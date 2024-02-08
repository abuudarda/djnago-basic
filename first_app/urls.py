from django.contrib import admin
from django.urls import path, re_path
from first_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^$',views.index,name='index'),
]
