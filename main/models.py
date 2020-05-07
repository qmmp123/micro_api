import binascii
import os

from django.db import models


# Create your models here.


class AppModel(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    additional_info = models.TextField(default="")

    def generate_new_api_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = self.generate_new_api_key()
        return super().save(*args, **kwargs)
