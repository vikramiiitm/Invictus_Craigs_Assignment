from rest_framework import fields, serializers
from .models import *

# class LocationSerialzer(serializers.Serializer):
#     class Meta:
#         model = Location
#         fields = "__all__"

class ProfileSerializer(serializers.Serializer):
    loc = serializers.StringRelatedField()

    class Meta:
        model=Profile
        fields = [
            'id',
            'loc',
            'userId',
            'price',
            'description',
            'status',
        ]
