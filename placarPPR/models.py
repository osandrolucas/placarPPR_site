from django.db import models
from django.utils import timezone

class Post(models.Model):
    publicador = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    meta_ano = models.CharField(max_length=20)
    meta_acum = models.CharField(max_length=20)
    real_acum = models.CharField(max_length=20)
    percent_ating = models.CharField(max_length=10)
    atingido_ano = models.CharField(max_length=10)
    farol = models.CharField(max_length=10)
    qt_salarios = models.CharField(max_length=5)
    obs = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
