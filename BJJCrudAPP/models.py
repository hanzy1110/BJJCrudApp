from django.db import models


class Student(models.Model):
    id = models.BigAutoField()
    date_of_birth = models.DateField()
    personal_id = models.CharField(max_length=10)
    belt_colour = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    academy = models.CharField(max_length=50)

    def __str__(self):
        return self.personal_id
