from django.http import JsonResponse
from django.http import HttpRequest
from . import models
import json

# 登录
def login(request):
    param = json.loads(request.body)
    userName = param['userName']
    password = param['password']

    respCode = '01'
    respMsg = '未知错误，无法登录'

    user = models.BladeUser.objects.get(account=userName)
    
    print(user.password)

    resp = {'respCode': respCode, 'respMsg': respMsg}
    return JsonResponse(resp)

