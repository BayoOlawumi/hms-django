from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=(
            'email',
            'name',
            'phone_number',
            'is_active',
            'date_in',
            'date_out',
        )
