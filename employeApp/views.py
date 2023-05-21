from django.shortcuts import render
from employeApp.models import employee,Department
from employeApp.serializers import EmployeeSerializers,DepartmentSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import viewsets
# Create your views here.

@csrf_exempt

def EmployeeAPI(request,id=0):
        if request.method=="GET":
          Employee_data=employee.objects.all()
          employee_serializer=EmployeeSerializers(Employee_data,many=True)
          return JsonResponse(employee_serializer.data,safe=False) 
        
        elif request.method=="POST":
          Employee_data=JSONParser().parse(request)
          obj= EmployeeSerializers(data=Employee_data)
          if obj.is_valid():
            obj.save()
            return JsonResponse("Data Saved Succesfully", safe=False)
          return JsonResponse("Invalid Data.........!", safe=False)
        
        elif request.method=="PUT":
            edit_data=JSONParser().parse(request)
            obj=EmployeeSerializers(data=edit_data)
            if obj.is_valid():
                obj.save()
                return JsonResponse("Data Updated Succusfully......",safe=False)
            return JsonResponse("Invalid data.......!")
        elif request.method=="DELETE":
          delete_data= JSONParser().parse(request)
        
          obj =employee.objects.get(Id=delete_data['Id'])
          obj.delete()
          return JsonResponse("Data deleted.....!", safe=False)



class EmployeeView(viewsets.ModelViewSet):
   queryset = employee.objects.all()
   serializer_class = EmployeeSerializers

@csrf_exempt
def Department_Data(request,id=0):
        if request.method=="GET":
          department_data=Department.objects.all()
          department_serializer=DepartmentSerializers(department_data, many=True)
          return JsonResponse(department_serializer.data, safe=False) 
        
        elif request.method=="POST":
          department_data=JSONParser().parse(request)
          obj= DepartmentSerializers(data=department_data)
          if obj.is_valid():
            obj.save()
            return JsonResponse("Data Saved Succesfully", safe=False)
          return JsonResponse("Invalid Data.........!")
        
        elif request.method=="PUT":
            edit_department=JSONParser().parse(request)
            department_data=Department.objects.get(Dep_id=edit_department['Dep_id'])
            obj=DepartmentSerializers(department_data,data=edit_department)
            if obj.is_valid():
                obj.save()
                return JsonResponse("Data Updated Succusfully......", safe=False)
            return JsonResponse("Invalid data.......!", safe=False)
        
        elif request.method=="DELETE":
          delete_department= JSONParser().parse(request)
        
          obj =Department.objects.get(Dep_id=delete_department['Dep_id'])
          obj.delete()
          return JsonResponse("Data deleted.....!", safe=False)
