from django.urls import path
from webapp.views import index, cat

urlpatterns = [
    path('', index),
    path('cat_stats/', cat)
]
