from rest_framework import fields, serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    loc = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = [
            "id",
            "loc",
            "userId",
            "price",
            "description",
            "status"
        ]
