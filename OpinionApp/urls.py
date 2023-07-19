from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('Login.html', views.Login, name="Login"), 
	       path('Register.html', views.Register, name="Register"),
	       path('Signup', views.Signup, name="Signup"),
	       path('UserLogin', views.UserLogin, name="UserLogin"),
	       path('EditProfile.html', views.EditProfile, name="EditProfile"), 
	       path('EditMyProfile', views.EditMyProfile, name="EditMyProfile"),
	       path('UpdateStatus.html', views.UpdateStatus, name="UpdateStatus"),
	       path('UpdateMyStatus', views.UpdateMyStatus, name="UpdateMyStatus"),
	       path('ChangePassword.html', views.ChangePassword, name="ChangePassword"),
	       path('ChangeMyPassword', views.ChangeMyPassword, name="ChangeMyPassword"),
	       path('PostTopic.html', views.PostTopic, name="PostTopic"),
	       path('PostMyTopic', views.PostMyTopic, name="PostMyTopic"),
	       path('HomePage.html', views.HomePage, name="HomePage"),
	       path('PostComment', views.PostComment, name="PostComment"),
	       path('PostMyComment', views.PostMyComment, name="PostMyComment")
]