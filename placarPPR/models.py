from django.db import models
from django.utils import timezone


class Post(models.Model):
    publicador = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=100)
    meta_ano = models.CharField('Meta do Ano', max_length=20)
    meta_acum = models.CharField('Meta Acumulada', max_length=20)
    real_acum = models.CharField('Real Acumulado', max_length=20)
    percent_ating = models.CharField('% Atingido', max_length=10)
    atingido_ano = models.CharField('Atingido Ano', max_length=10)
    farol = models.CharField('Farol', max_length=10)
    qt_salarios = models.CharField('Qt. Salários', max_length=5)
    obs = models.TextField('Observação')
    created_date = models.DateTimeField('Data de Criação',
                                        default=timezone.now)
    published_date = models.DateTimeField('Data de Publicação',
                                          blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Placar PPR'
        verbose_name_plural = 'Placares de PPR'


def publish(self):
    self.published_date = timezone.now()
    self.save()


