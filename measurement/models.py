from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название', null=False)
    description = models.CharField(max_length=50, verbose_name='Описание')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor',
                               verbose_name='Модель датчика')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
