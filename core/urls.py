from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='homepage'),
   path('submit',views.index_submit,name='temp_submit')
]