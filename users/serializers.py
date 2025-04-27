from django.core.validators import RegexValidator
from rest_framework import serializers
from users.models import User


# Serializers

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, validators=[
        RegexValidator(
            regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
            message="Atleast 8 character, atleast one uppercase letter, atleast one lowercase letter, atleast one number, atleast one special character."
        )
    ])

    class Meta:
        model = User
        fields = '__all__'

    
    # Hash password before User create
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email']
