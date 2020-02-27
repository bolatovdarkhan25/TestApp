from django.urls import path
from task_manager.api import views

app_name = 'task_manager'

urlpatterns = [
    path('tag/list/', views.TagsListAPIView.as_view(), name='tags_list'),
    path('task/list/', views.TasksListAPIView.as_view(), name='tasks_list'),
    path('tag/detail/<pk>/', views.TagDetailAPIView.as_view(), name='tag_detail'),
    path('task/detail/<pk>/', views.TaskDetailAPIView.as_view(), name='task_detail'),
    path('tag/create/', views.CreateTagAPIView.as_view(), name='tag_create'),
    path('task/create/', views.CreateTaskAPIView.as_view(), name='task_create'),
    path('tag/update/<pk>/', views.UpdateTagAPIView.as_view(), name='tag_update'),
    path('task/update/<pk>/', views.UpdateTaskAPIView.as_view(), name='task_update'),
    path('tag/delete/<pk>/', views.DeleteTagAPIView.as_view(), name='tag_delete'),
    path('task/delete/<pk>/', views.DeleteTaskAPIView.as_view(), name='task_delete'),
]