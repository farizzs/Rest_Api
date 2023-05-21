from rest_framework import serializers
from employeApp.models import employee,Department

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = (
            'Id',
            'Name',
            'Department',
            'Salary'   
        )
        extra_kwargs = {
            "Name":{
                "required": True,
                "max_length": 15
            }
        }

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'Dep_id',
            'Dep_name'
            
        )