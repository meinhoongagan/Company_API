from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializers,EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
     try:
        company=Company.objects.get(pk=pk)
        employee=Employee.objects.filter(company=company)
        emp_serializer=EmployeeSerializers(employee,many=True,context={'request':request})
        return Response(emp_serializer.data)
     except Exception as e:
        print(e)
        return Response({'message':'Compnay might not exist'})
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers