from django.urls import path
from . views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name='home'),
    path('user/<str:username>/',UserPostListView.as_view(), name='user'),
    path('post/<int:pk>/',PostDetailView.as_view(), name="detail"),
    path('post/new/',PostCreateView.as_view(), name="create"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name="delete"),
    path("about/",views.about, name="about")
]
