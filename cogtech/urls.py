from django.urls import path
from cogtech.views import index

urlpatterns = [
    path('', index)
]