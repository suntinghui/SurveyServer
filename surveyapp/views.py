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

    except:
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

    except:
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
        
    except:
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

    except:
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


    except:
        respCode = '04'
        respMsg = '未知错误，请重试'
        resp = {'respCode': respCode, 'respMsg': respMsg}

    return JsonResponse(resp)




















