from __future__ import unicode_literals

from django.db import models


class Gato(models.Model):
    name = models.CharField(max_length=266)
    patas = models.IntegerField(default=4)

    def __str__(self):
        return self.name
