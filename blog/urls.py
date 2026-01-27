from django.urls import path
from mysite.views.post_view import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home')
]
