
from django.contrib import admin
from django.urls import path
from wordcount.views import home, about, count

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('count/', count, name="count"),
]
