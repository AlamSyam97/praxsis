from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('',views.readMakanan, name='readMakanan'),
    path('hapus/<id>',views.hapus, name='hapus'),
    path('edit/<id>',views.edit, name='edit'),
    path('detail/<id>',views.detail, name='detail')
]
