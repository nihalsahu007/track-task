from rest_framework import serializers
from .models import Task, TaskActivityLog

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivityLog
        fields = '__all__'
