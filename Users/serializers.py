from rest_framework import serializers
from .models import UserProfile
from Rooms.serializers import RoomSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    rooms_created = RoomSerializer(many=True, read_only= True)
    class Meta:
        model=UserProfile
        fields=(
            'email',
            'name',
            'is_staff',
            'is_active',
            'rooms_created',
        )
