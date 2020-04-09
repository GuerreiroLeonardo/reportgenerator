from django.db import models

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
    
    class Meta:
        verbose_name = 'Mercado'
        verbose_name_plural = 'Mercados'
        ordering = ['-market_name']