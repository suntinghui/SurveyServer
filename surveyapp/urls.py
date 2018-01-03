from django.urls import path
from . import views

urlpatterns = [
    path('api/login.json', views.login),
    path('projectInterController/projectList.json', views.projectList),
    path('api/getDictList.json', views.getDictList),
    path('taskInterController/taskList.json', views.taskList),
    path('engineroomInterController/queryEngineroomInfo.json', views.queryEngineroomInfo),
    path('engineroomInterController/updateEngineroomInfo.json', views.updateEngineroomInfo),
    path('geospatialInterController/geospatialList.json', views.geospatialList),



    
]