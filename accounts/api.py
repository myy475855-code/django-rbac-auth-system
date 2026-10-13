from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminRole, IsCompanyOrAdmin, IsStudentOrAdmin
class MeAPI(APIView):
 permission_classes=[IsAuthenticated]
 def get(self,request): return Response({"id":request.user.id,"username":request.user.username,"email":request.user.email,"groups":list(request.user.groups.values_list("name",flat=True))})
class StudentAPI(APIView):
 permission_classes=[IsStudentOrAdmin]
 def get(self,request): return Response({"message":"Student API access granted.","role":"Student"})
class CompanyAPI(APIView):
 permission_classes=[IsCompanyOrAdmin]
 def get(self,request): return Response({"message":"Company API access granted.","role":"Company"})
class AdminAPI(APIView):
 permission_classes=[IsAdminRole]
 def get(self,request): return Response({"message":"Admin API access granted.","role":"Admin"})
