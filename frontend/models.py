from django.db import models


# Create your models here.


class BTCUSExchange(models.Model):
    # time_period_start = models.CharField(max_length=200, blank=True)
    # time_period_end = models.CharField(max_length=200, blank=True)
    # time_open = models.CharField(max_length=200, blank=True)
    # time_close = models.CharField(max_length=200, blank=True)
    # rate_open = models.CharField(max_length=200, blank=True)
    # rate_high = models.CharField(max_length=200, blank=True)
    # rate_low = models.CharField(max_length=200, blank=True)
    # rate_close = models.CharField(max_length=200, blank=True)
    time_period_start = models.DateTimeField()
    time_period_end = models.DateTimeField()
    time_open = models.DateTimeField()
    time_close = models.DateTimeField()
    rate_open = models.DecimalField(max_digits=10, decimal_places=2)
    rate_high = models.DecimalField(max_digits=10, decimal_places=2)
    rate_low = models.DecimalField(max_digits=10, decimal_places=2)
    rate_close = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "BTC US Exchange"
        verbose_name_plural = "BTC US Exchange"


class Task(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
