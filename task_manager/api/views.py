from django.shortcuts import render, get_object_or_404
from task_manager.models import Tag, Task
from rest_framework import generics
from task_manager.api import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView


# Create your views here.


def tags_views(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags})


def tasks_views(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})


class TagsListAPIView(generics.ListAPIView):
    serializer_class = serializers.TagListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class TasksListAPIView(generics.ListAPIView):
    serializer_class = serializers.TaskListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TagDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.TagDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class TaskDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.TaskDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class CreateTagAPIView(generics.CreateAPIView):
    serializer_class = serializers.TagCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateTaskAPIView(generics.CreateAPIView):
    serializer_class = serializers.TaskCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateTagAPIView(generics.UpdateAPIView):
    serializer_class = serializers.TagCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get(self, pk):
        serializer = serializers.TagDetailSerializer(get_object_or_404(Tag, user=self.request.user, pk=pk))
        return Response(serializer.data)


class UpdateTaskAPIView(generics.UpdateAPIView):
    serializer_class = serializers.TaskCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get(self, pk):
        serializer = serializers.TaskDetailSerializer(get_object_or_404(Task, user=self.request.user, pk=pk))
        return Response(serializer.data)


class DeleteTagAPIView(generics.DestroyAPIView):
    serializer_class = serializers.TagCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        serializer = serializers.TagDetailSerializer(get_object_or_404(Tag, user=self.request.user, pk=kwargs['pk']).delete())
        return Response(serializer.data)


class DeleteTaskAPIView(generics.DestroyAPIView):
    serializer_class = serializers.TaskCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        serializer = serializers.TaskDetailSerializer(get_object_or_404(Task, user=self.request.user, pk=kwargs['pk']).delete())
        return Response(serializer.data)

