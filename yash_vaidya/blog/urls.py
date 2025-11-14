from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    # path('post/list', views.post_list, name='post_list'),
    path('path/<int:post_id>/',views.post_details, name = "post_details"),
    path('path/create/', views.post_create, name = 'post_create'),
    path('post/<int:post_id>/edit', views.post_update, name = 'post_update'),
    path('post/<int:post_id>/delete', views.post_delete, name = 'post_delete'),

    path('myposts/', views.user_post, name='my_posts'),
    path('draftpost/', views.draft_posts, name='draft_post'),

    path('register/', views.register, name = 'register'),
    
    path('profile/', views.about, name = 'profile'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
     
]

