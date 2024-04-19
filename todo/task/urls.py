from django.urls import path
from .views import TaskCreateAPIView

urlpatterns = [
    path('', TaskCreateAPIView.as_view(), name='column-create'),
]