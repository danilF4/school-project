from . import views
from django.conf.urls import include, url
from django.urls import include, path
#from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'), # done
	path('register/', views.RegisterView.as_view(), name='register'), # done
	path('logout/', views.logout_view, name='logout'), # done
	url(r'^profile-edit/(?P<username_>[\w-]+)/$', views.edit_profile, name='profile-edit'), # i have no idea what to do
	url(r'^profile/f/liked_posts/$', views.liked_posts, name='liked_posts'), # done
	url(r'^profile/(?P<username_>[\w-]+)/$', views.profile, name='profile'),
	url(r'^top-users/$', views.top_users, name='top-users'),
]