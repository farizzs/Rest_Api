from django.conf.urls import url
from django.urls import path, include
from employeApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeeView, 'employee')

urlpatterns=[

    url(r'^EmployeeAPI/',views.EmployeeAPI),
    url(r'^EmployeeAPI/([0-9]+)$',views.EmployeeAPI),
    url(r'^Department/',views.Department_Data),
    url(r'^Department/([0-9]+)$',views.Department_Data),
]

