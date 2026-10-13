from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import RegisterForm
from .permissions import has_role
def home(request): return render(request,"accounts/home.html")
def register(request):
 if request.user.is_authenticated: return redirect("dashboard")
 if request.method=="POST":
  form=RegisterForm(request.POST)
  if form.is_valid():
   user=form.save(); group,_=Group.objects.get_or_create(name="Student"); user.groups.add(group)
   login(request,user); messages.success(request,"Your account has been created."); return redirect("dashboard")
 else: form=RegisterForm()
 return render(request,"accounts/register.html",{"form":form})
@login_required
def dashboard(request):
 roles=[r for r in ("Student","Company","Admin") if has_role(request.user,r)]
 return render(request,"accounts/dashboard.html",{"roles":roles})
@login_required
def student_dashboard(request):
 if not has_role(request.user,"Student"): return render(request,"accounts/forbidden.html",status=403)
 return render(request,"accounts/role_dashboard.html",{"role":"Student","description":"Access student-only resources and account information."})
@login_required
def company_dashboard(request):
 if not has_role(request.user,"Company"): return render(request,"accounts/forbidden.html",status=403)
 return render(request,"accounts/role_dashboard.html",{"role":"Company","description":"Manage company resources and candidate workflows."})
@login_required
def admin_dashboard(request):
 if not has_role(request.user,"Admin"): return render(request,"accounts/forbidden.html",status=403)
 return render(request,"accounts/role_dashboard.html",{"role":"Admin","description":"Review user roles and oversee access."})
