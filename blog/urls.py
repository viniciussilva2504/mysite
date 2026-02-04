from django.urls import path
from blog.views import home, PostView, PostDetailView

urlpatterns = [
    path('', home, name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
