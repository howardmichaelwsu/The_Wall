from django.urls import path
from . import views

urlpattern = [ 
	path('', views.index),
	path('register', views.register),
	path('login', views.login),
	path('success', views.success),
	path('logout', views.logout),
	path('messages', views.messaging),
	path('add_comment/<int:id>', views.post_comment),
	path('user_profile/<int:id>', views.user_profile),
	path('like/<int:id>', views.likes),
	path('delete_comment<int:id>', views.delete_comment),
	path('edit/<int:id>', views.edit),
]