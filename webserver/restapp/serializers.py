from restapp.models import Info
from rest_framework.serializers import ModelSerializer

class RestSerializer(ModelSerializer):
    class Meta:
        model=Info
        fields=['url','email']

