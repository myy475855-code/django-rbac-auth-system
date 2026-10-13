from django.contrib.auth.models import Group,User
from django.test import TestCase
class RBACAPITests(TestCase):
 @classmethod
 def setUpTestData(cls):
  for role in ("Student","Company","Admin"): Group.objects.get_or_create(name=role)
  for username,role in (("stu","Student"),("co","Company"),("adm","Admin")):
   u=User.objects.create_user(username=username,password="StrongPass!123"); u.groups.add(Group.objects.get(name=role))
 def test_student_api_allowed(self):
  self.client.login(username="stu",password="StrongPass!123"); self.assertEqual(self.client.get("/api/student/").status_code,200)
 def test_student_cannot_access_company_api(self):
  self.client.login(username="stu",password="StrongPass!123"); self.assertEqual(self.client.get("/api/company/").status_code,403)
 def test_company_api_allowed(self):
  self.client.login(username="co",password="StrongPass!123"); self.assertEqual(self.client.get("/api/company/").status_code,200)
 def test_admin_can_access_all(self):
  self.client.login(username="adm",password="StrongPass!123")
  for url in ("/api/student/","/api/company/","/api/admin/"): self.assertEqual(self.client.get(url).status_code,200)
 def test_student_page_denied_to_company(self):
  self.client.login(username="co",password="StrongPass!123"); self.assertEqual(self.client.get("/dashboard/student/").status_code,403)
