from rest_framework.permissions import BasePermission
def has_role(user, role):
 if not user or not user.is_authenticated: return False
 return user.is_superuser or user.groups.filter(name__in=[role,"Admin"]).exists()
class IsStudentOrAdmin(BasePermission):
 message="Student role required."
 def has_permission(self,request,view): return has_role(request.user,"Student")
class IsCompanyOrAdmin(BasePermission):
 message="Company role required."
 def has_permission(self,request,view): return has_role(request.user,"Company")
class IsAdminRole(BasePermission):
 message="Admin role required."
 def has_permission(self,request,view): return bool(request.user and request.user.is_authenticated and (request.user.is_superuser or request.user.groups.filter(name="Admin").exists()))
