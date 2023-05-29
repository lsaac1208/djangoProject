from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('search/', views.search, name='search'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('manage_posts/<int:user_id>/', views.manage_posts, name='manage_posts'),
    path('settings/<int:user_id>/', views.settings, name='settings'),
]
