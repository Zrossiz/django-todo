from django.urls import path
from .views import TaskCreateAPIView

urlpatterns = [
    path('', TaskCreateAPIView.as_view(), name='task-create'),
    path('<int:pk>/', TaskCreateAPIView.as_view(), name='task-update'),
    path('<int:pk>', TaskCreateAPIView.as_view(), name='task-delete')
]