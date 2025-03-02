from rest_framework import serializers
from user.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

# User create, update, delete serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'full_name', 'role', 'id', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            full_name=validated_data['full_name'],
            role=validated_data['role'],
            password=validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.role = validated_data.get('role', instance.role)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
    
    
# Login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    
    class Meta:
        fields = ('username', 'password')
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        # Return only relevant user details
        return {'username': user.username, 'full_name': user.full_name, 'role': user.role, 'id': user.id}


# Logout serializer
class LogoutSerializer(serializers.Serializer):
    pass