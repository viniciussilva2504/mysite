from django.urls import path
from config.views.post_view import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home')
]
