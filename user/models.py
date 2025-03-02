from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    MANAGER = "manager", "Manager"
    SERVICE_MANAGER = "service_manager", "Service Manager"
    TEAMLEAD = "teamlead", "Teamlead"
    WORKER = "worker", "Worker"

class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.WORKER
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
