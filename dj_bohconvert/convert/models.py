from django.db import models

class Convert(models.Model):
    id = models.AutoField(primary_key=True)
    decimal = models.DecimalField(max_digits=10, decimal_places=2)
    precisao = models.IntegerField()
    binario = models.CharField(max_length=255)
    octal = models.CharField(max_length=255)
    hexadecimal = models.CharField(max_length=255)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.decimal} - {self.precisao}'