from django.db import models


class Proj2Model(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):  # __unicode__ for python2
        return self.name
