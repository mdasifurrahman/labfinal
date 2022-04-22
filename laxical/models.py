from django.db import models

# Create your models here.
class symbol_table(models.Model):
    s_name = models.CharField(max_length=20)
    token_type = models.CharField(max_length=30)
