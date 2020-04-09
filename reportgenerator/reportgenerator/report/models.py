from django.db import models
from django.utils import timezone
import datetime
class Market(models.Model):
    market_id = models.CharField(
        verbose_name='Market id',
        max_length = 200
        )
    market_name = models.CharField(
        verbose_name='Nome do Mercado',
        max_length=200
        )

    objects = models.Manager()
    
    created_at = models.DateTimeField(
        verbose_name='Criado em',
        default = datetime.datetime.now,
        )

    def __str__(self):
        return self.market_name

    class Meta:
        verbose_name = 'Mercado'
        verbose_name_plural = 'Mercados'
        ordering = ['-market_name']