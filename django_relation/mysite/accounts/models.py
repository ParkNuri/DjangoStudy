from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser 
# Create your models here.

# AUTH_USER_MODEL는 settings.py에서 설정
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="followings",
        blank=True
    )
    # 각종 필드들 추가하면
    # createsuperuser 못 만듬
    # db지우고 만들게되면
    # shell_plus에서 create_user is_staff, 최고권한 True
    # User.objects.create_user(username='admin', password='1234', is_staff=True)
    # 먼저 해주기