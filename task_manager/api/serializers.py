from rest_framework import serializers
from task_manager.models import Tag, Task
from users.api import serializers as users_serializers


class TagListSerializer(serializers.ModelSerializer):
    user = users_serializers.UserSerializer(read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    user = users_serializers.UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TagDetailSerializer(serializers.ModelSerializer):
    tasks = TaskListSerializer(read_only=True, many=True)
    user = users_serializers.UserDetailSerializer(read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'user', 'slug', 'date_of_creation', 'tasks']


class TaskDetailSerializer(serializers.ModelSerializer):
    tags = TagListSerializer(read_only=True, many=True)
    user = users_serializers.UserDetailSerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'user',
            'slug',
            'description',
            'date_of_creation',
            'tags',
            'start_time',
            'deadline',
        ]


class TagCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name',
        ]


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'tags',
            'start_time',
            'deadline',
        ]