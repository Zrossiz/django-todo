from django.urls import path
from .views import ColumnCreateAPIView

urlpatterns = [
    path('', ColumnCreateAPIView.as_view(), name='column-create'),
]