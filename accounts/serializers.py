from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
