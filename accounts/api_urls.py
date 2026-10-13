from django.urls import path
from .api import MeAPI, StudentAPI, CompanyAPI, AdminAPI
urlpatterns=[path("me/",MeAPI.as_view()),path("student/",StudentAPI.as_view()),path("company/",CompanyAPI.as_view()),path("admin/",AdminAPI.as_view())]
