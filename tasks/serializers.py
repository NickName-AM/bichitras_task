from rest_framework import serializers
from rest_framework.response import Response

from tasks.models import Task
from users.models import User

# Serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status"]
    
    def create(self, validated_data):
        user = self.context['request'].user
        task = Task(user=user, **validated_data)
        task.save()
        return task
