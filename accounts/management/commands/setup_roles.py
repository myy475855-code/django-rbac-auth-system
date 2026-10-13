from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group,Permission
class Command(BaseCommand):
 help="Create standard RBAC groups."
 def handle(self,*args,**kwargs):
  for name in ("Student","Company","Admin"):
   group,created=Group.objects.get_or_create(name=name)
   if name=="Admin":
    group.permissions.add(*Permission.objects.filter(content_type__app_label__in=("auth","accounts")))
   self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Ensured'} group: {name}"))
