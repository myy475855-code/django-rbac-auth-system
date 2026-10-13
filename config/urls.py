from django.contrib import admin
from django.urls import path, include
from accounts import views
urlpatterns = [
 path("admin/",admin.site.urls), path("",views.home,name="home"),
 path("accounts/",include("django.contrib.auth.urls")),
 path("accounts/register/",views.register,name="register"),
 path("dashboard/",views.dashboard,name="dashboard"),
 path("dashboard/student/",views.student_dashboard,name="student_dashboard"),
 path("dashboard/company/",views.company_dashboard,name="company_dashboard"),
 path("dashboard/admin/",views.admin_dashboard,name="admin_dashboard"),
 path("api/",include("accounts.api_urls")),
]
