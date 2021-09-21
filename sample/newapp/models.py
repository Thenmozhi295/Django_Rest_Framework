from django.db import models
from django.db.models.fields import CharField

class health(models.Model):
      fruit = models.CharField(max_length=10)
      size = models.CharField(max_length=25)
      color = models.CharField(max_length=10)
      class Meta:
          managed = False
          db_table = 'dataframe_values'