from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index.html', views.index),
    path('product.html',views.product),
    path('contact.html',views.contact),
    path('menu.html',views.menu),

]
