from django.db import models


class Student(models.Model):
    name = models.CharField(
        verbose_name="Nombre", max_length=50, blank=False, null=True
    )
    surname = models.CharField(
        verbose_name="Apellido", max_length=50, blank=False, null=True
    )
    date_of_birth = models.DateField(verbose_name="Fecha Nacimiento")
    personal_id = models.CharField(verbose_name="DNI", max_length=10)
    belt_colour = models.CharField(verbose_name="Faixa", max_length=20)
    weight = models.DecimalField(verbose_name="Peso", max_digits=5, decimal_places=1)
    monto_pago = models.DecimalField(
        verbose_name="monto_pago", max_digits=10, decimal_places=1, default=0
    )
    academy = models.CharField(verbose_name="Academia", max_length=50)
    clase = models.CharField(verbose_name="Clase", max_length=50)
    absoluto = models.BooleanField(
        verbose_name="Absoluto", max_length=50, default=False
    )

    def __str__(self):
        return self.personal_id
