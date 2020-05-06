from django.db import models


# Create your models here.


class AppModel(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)

    def generate_new_api_key(self):
        pass
