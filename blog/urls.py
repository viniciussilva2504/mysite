from django.urls import path
from views.post_view import PostView, PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
