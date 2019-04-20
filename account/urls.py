from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#path('login/', views.user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('', views.dashboard, name='dashboard'),
	path('register/', views.register, name='register'),
	path('edit/', views.edit, name='edit'),
	path('users/', views.user_list, name='user_list'),
	path('users/<username>/', views.user_detail, name='user_detail'),
	path('friend_request/', views.flist, name='friends_req'),
	path('users/<username>/request', views.frequest, name='friend_request'),
	path('friend_request/<username>/confirm', views.fconfirm, name='friend_confirm'),
	path('friend_request/<username>/reject', views.freject, name='friend_reject'),
	path('friends/', views.fl, name='friends')
]