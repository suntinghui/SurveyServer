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
    path('rackinfoInterController/rackList.json', views.rackList),
    path('rackinfoInterController/addRackInfo.json', views.addRackInfo),
    path('rackinfoInterController/updateRackInfo.json', views.updateRackInfo),
    path('rackinfoInterController/deleteRackInfo.json', views.deleteRackInfo),
    path('facilityInterController/queryFacility.json', views.queryFacility),
    path('facilityInterController/addFacility.json', views.addFacility),
    path('facilityInterController/updateFacility.json', views.updateFacility),
    path('facilityInterController/deleteFacility.json', views.deleteFacility),
    path('airConditioningInterController/queryAirConditioning.json', views.queryAirConditioning),
    path('airConditioningInterController/addAirConditioning.json', views.addAirConditioning),
    path('airConditioningInterController/updateAirConditioning.json', views.updateAirConditioning),
    path('airConditioningInterController/deleteAirConditioning.json', views.deleteAirConditioning),
    



    
]