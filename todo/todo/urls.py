
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('column/', include('column.urls')),
    path('task/', include('task.urls'))
]
