from django.db import models
from django.contrib.auth.models import AbstractUser

UserTypeChoise = (
    (0, "Simple User"),
    (1, "Admin")
)


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    status = models.SmallIntegerField(default=0, choices=UserTypeChoise)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Company(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    url_redirect = models.URLField(blank=True, null=True)
    secret_key = models.CharField(max_length=255)
    allowed_domain = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ShareAction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
