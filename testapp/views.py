from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authetication import TokenAuthentication
from rest_framework.permissions import * 
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,djangoModelPermissions,DjangoModelPremissionsOrAnonReadOnly
from testapp.permissions import IsReadOnly

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication,]
    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly,]
    permission_classes=[IsReadOnly,]