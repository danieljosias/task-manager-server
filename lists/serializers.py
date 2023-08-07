from rest_framework import serializers
from .models import List
from users.models import User
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404

class ListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = List
        fields = ['id', 'title', 'user', 'user_id',]
        read_only_fields = ['id']


    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user_found = get_object_or_404(User, id = user_id)

        new_list = List.objects.create(**validated_data, user=user_found)

        return new_list
    

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()

        super().update(instance, validated_data)
        return instance
        