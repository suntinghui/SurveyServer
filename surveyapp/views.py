from django.http import JsonResponse
from django.http import HttpRequest
from . import models
from . import utils # 自定义的工具类
import json

# 登录
def login(request):
    print("login:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    password = param['password']

    respCode = '01'
    respMsg = '未知错误，无法登录'

    try:
        user = models.BladeUser.objects.get(account=userName)

        if not utils.djCheckPwd(password, user.password):
            respCode = '03'
            respMsg = '用户名或密码错误'

        else:
            respCode = '00'
            respMsg = '登录成功'


    except models.BladeUser.DoesNotExist:
        respCode = '04'
        respMsg = '账号不存在'


    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询项目列表
def projectList(request):
    print("projectList:", request.body)
    param = json.loads(request.body)
    userName = param['userName']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Project.objects.filter(project_manager=userName).values()

        respCode = '00'
        respMsg = '查询成功'

        resp = {'respCode': respCode, 'respMsg': respMsg, 'proList':list(vs)}

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '未知错误，请重试'
        resp = {'respCode': respCode, 'respMsg': respMsg}
        
    return JsonResponse(resp)

# 查询数据字典
def getDictList(request):
    respCode = '04'
    respMsg = '未知错误，请重试'

    dictData = {}

    try:
        for key, value in utils.dataDic().items():
            itemData = {}

            vs0 = models.BladeDict.objects.filter(code=key)

            vs1 = vs0.filter(pid = 0)

            itemData["code"] = key
            itemData["name"] = vs1[0].name

            vs2 = vs0.exclude(pid = 0).values()
            itemData["dictList"] = list(vs2)

            dictData[value] = itemData

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'dictData':dictData}

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '未知错误，请重试'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 查询任务列表
def taskList(request):
    print("projectList:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    proId = param['proId']

    respCode = '04'
    respMsg = '未知错误，请重试'

    sqlRaw = """
        SELECT
        t.* ,(SELECT NAME FROM allot_item WHERE t.project_code=project_code) AS itename
        ,(SELECT NAME FROM blade_user WHERE t.prospecting=id) AS prname
        ,(SELECT NAME FROM blade_user WHERE t.plan=id) AS planname
        ,(SELECT NAME FROM blade_user WHERE t.test=id) AS testname
        ,(SELECT NAME FROM blade_user WHERE t.construction=id) AS conrname,e.NAME as statename
        FROM  project_task t 
        LEFT JOIN (SELECT num,NAME FROM blade_dict WHERE CODE=138) e ON t.`task_state`=e.num 
        WHERE t.prospecting='%s' AND t.project_code='%s' """ % (userName, proId)

    try:
        vs = models.ProjectTask.objects.raw(sqlRaw)

        taskList = []
        for item in vs:
            itemJson = json.dumps(item, default=lambda obj: obj.__dict__)
            taskList.append(itemJson)


        respCode = '00'
        respMsg = '查询成功'

        resp = {'respCode': respCode, 'respMsg': respMsg, 'taskList':taskList}
        
    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '未知错误，请重试'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询机房信息
def queryEngineroomInfo(request):
    print("queryEngineroomInfo:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Engineroom.objects.get(engroom_code=engineroom_id)

        respCode = '00'
        respMsg = '查询成功'

        resp = {'respCode': respCode, 'respMsg': respMsg}

        for key, value in vs.__dict__.items():
            if '_state' == key:
                continue

            resp[key] = "" if value==None else value

    except models.Engineroom.DoesNotExist:
        respCode = '03'
        respMsg = '该机房信息不存在'

        resp = {'respCode': respCode, 'respMsg': respMsg}
        
    return JsonResponse(resp)

# 修改机房信息
def updateEngineroomInfo(request):
    print("updateEngineroomInfo:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    try:
        obj = models.Engineroom.objects.get(engroom_code=engineroom_id)

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 查询机楼列表
def geospatialList(request):
    print("geospatialList:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Geospatial.objects.all().values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'buildList':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '未知错误，请重试'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询机架列表
def rackList(request):
    print("rackList:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Rack.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'rackList':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 添加机架信息
def addRackInfo(request):
    print('addRackInfo:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        rack = models.Rack.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新机架信息
def updateRackInfo(request):
    print('updateRackInfo:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.Rack.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除机架信息
def deleteRackInfo(request):
    print('deleteRackInfo:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.Rack.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询主设备列表
def queryFacility(request):
    print("queryFacility:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Facility.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 添加主设备
def addFacility(request):
    print('addFacility:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.Facility.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 修改主设备
def updateFacility(request):
    print('updateFacility:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.Facility.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)
    

# 删除主设备
def deleteFacility(request):
    print('deleteFacility:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.Facility.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询制冷设备列表
def queryAirConditioning(request):
    print("queryAirConditioning:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Airconditioning.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 添加制冷设备
def addAirConditioning(request):
    print('addAirConditioning:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.Airconditioning.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新制冷设备
def updateAirConditioning(request):
    print('updateAirConditioning:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.Airconditioning.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除制冷设备
def deleteAirConditioning(request):
    print('deleteAirConditioning:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.Airconditioning.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询制冷室外机列表
def queryAirOutDoor(request):
    print("queryAirOutDoor:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.OutdoorsMachine.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 添加制冷室外机
def addAirOutDoor(request):
    print('addAirOutDoor:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.OutdoorsMachine.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新制冷室外机
def updateAirOutDoor(request):
    print('updateAirOutDoor:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.OutdoorsMachine.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除制冷室外机
def deleteAirOutDoor(request):
    print('deleteAirOutDoor:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.OutdoorsMachine.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询配电柜列表
def queryDistributors(request):
    print("queryDistributors:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Distributors.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 添加配电柜
def addDistributors(request):
    print('addDistributors:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.Distributors.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新配电柜
def updateDistributors(request):
    print('updateDistributors:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.Distributors.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除配电柜
def deleteDistributors(request):
    print('deleteDistributors:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.Distributors.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询整流器列表
def queryRectifier(request):
    print("queryDistributors:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Rectifier.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 添加整流器
def addRectifier(request):
    print('addRectifier:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.Rectifier.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新整流器
def updateRectifier(request):
    print('updateRectifier:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.Rectifier.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除整流器
def deleteRectifier(request):
    print('deleteRectifier:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.Rectifier.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询UPS列表
def queryUps(request):
    print("queryUps:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Ups.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 添加Ups
def addUps(request):
    print('addUps:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.Ups.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新UPS
def updateUps(request):
    print('updateUps:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.Ups.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除UPS
def deleteUps(request):
    print('deleteUps:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.Ups.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询电池列表
def queryBattery(request):
    print("queryBattery:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Battery.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 添加电池组
def addBattery(request):
    print('addBattery:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.Battery.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新电池组
def updateBattery(request):
    print('updateBattery:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.Battery.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除电池组
def deleteBattery(request):
    print('deleteBattery:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.Battery.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询列头柜列表
def queryColheadcabinet(request):
    print("queryColheadcabinet:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.Colheadcabinet.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 添加列头柜
def addColheadcabinet(request):
    print('addColheadcabinet:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.Colheadcabinet.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新列头柜
def updateColheadcabinet(request):
    print('updateColheadcabinet:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.Colheadcabinet.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除列头柜
def deleteColheadcabinet(request):
    print('deleteColheadcabinet:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.Colheadcabinet.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 查询设备规格列表
def queryFacilityPlot(request):
    print("queryFacilityPlot:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.FacilityPlot.objects.all().values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 添加设备规格
def addFacilityPlot(request):
    print('addFacilityPlot:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")
        param.pop("engineroom_id")

        facility = models.FacilityPlot.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新设备规格
def updateFacilityPlot(request):
    print('updateFacilityPlot:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.FacilityPlot.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除设备规格
def deleteFacilityPlot(request):
    print('deleteFacilityPlot:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.FacilityPlot.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)


# 查询机柜列表
def queryMaccolInfo(request):
    print("queryMaccolInfo:", request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']

    respCode = '04'
    respMsg = '未知错误，请重试'

    try:
        vs = models.MachineColumn.objects.filter(engineroom_id=engineroom_id).values()

        respCode = '00'
        respMsg = '查询成功'
        resp = {'respCode': respCode, 'respMsg': respMsg, 'list':list(vs)}


    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '查询失败'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)

# 添加机柜
def addMaccolInfo(request):
    print('addMaccolInfo:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    respCode = "04"
    respMsg = '未知错误，请重试'

    try:
        # 表中不存在userName这一字段，所以必须要将其除
        param.pop("userName")

        facility = models.MachineColumn.objects.create(**param)
        respCode = "00"
        respMsg = '添加成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '添加失败'
        
    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

# 更新机柜
def updateMaccolInfo(request):
    print('updateMaccolInfo:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        obj = models.MachineColumn.objects.get(id=param["id"])

        for key, value in param.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()

        respCode = '00'
        respMsg = '修改成功'

    except Exception as e:
        print(e)

        respCode = '04'
        respMsg = '修改失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)


# 删除机柜
def deleteMaccolInfo(request):
    print('deleteMaccolInfo:', request.body)
    param = json.loads(request.body)
    userName = param['userName']
    engineroom_id = param['engineroom_id']
    
    try:
        models.MachineColumn.objects.filter(id=param["id"]).delete()

        respCode = '00'
        respMsg = '删除成功'

    except:
        respCode = '04'
        respMsg = '删除失败'

    resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)






        




















