from django.contrib import admin
from django.urls import include, path

from chat.views import index

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path("", index, name='index')
]