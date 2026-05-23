from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'
