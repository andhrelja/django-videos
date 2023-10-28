from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


USER_TYPE_CHOICES = (
    ('ADMIN', 'Administrator'),
    ('STUDENT', 'Student'), 
    ('TEACHER', 'Teacher'),
    ('PARENT', 'Parent')
)

class User(AbstractUser):
    user_type = models.CharField(_("User type"), choices=USER_TYPE_CHOICES, max_length=50)
