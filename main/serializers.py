from rest_framework import serializers

from main.models import AppModel


class AppModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppModel
        fields = ['id', 'api_key', 'additional_info']
