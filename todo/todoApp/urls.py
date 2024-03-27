from django.contrib import admin
from django.urls import path
from django.views import debug
from todoApp import views
from django.contrib.auth import views as auth_views

# Don't forget the commas at the end.
urlpatterns = [
    #path('', debug.default_urlconf), # returns the default page for / end-point

    # make the default end-point return our homepage instead
    path('', views.homepage, name='homepage'),
    path('test101/', views.test101, name='test101'), # test
    path('register/', views.register, name='register'), # register/ end-point
    path('my_login/', views.my_login, name='my_login'), # my_login/ end-point
    path('dashboard/', views.dashboard, name='dashboard'), # dashboard/ end-point
    path('my_logout/', views.my_logout, name='my_logout'), # my_logout/ end-point

    # CRUD operations
    path('create/', views.create, name='create'), # create/ end-point
    path('read/', views.read_all, name='read'), # read/ end-point
    path('update/<str:pk>', views.toupdate, name='update'), # update/ end-point
    path('delete/<str:pk>', views.todelete, name='delete'), # delete/ end-point

    # Profile management
    path('profile_management/', views.profile_management, name='profile_management'), # profile_management/ end-point
    path('delete_profile/', views.delete_profile, name='delete_profile'), # delete_profile/ end-point

    #Password Mangement
    
    #1 Allows us to enter our email in order to receive a password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="todoApp/reset_password.html"), name='reset_password',),
    #2 Shows success message saying the email was sent
    path('reset_password_sent/', auth_views.PasswordChangeDoneView.as_view(template_name="todoApp/reset_password_sent.html"), name='password_reset_done'),
    #3 Sends a link to our email in order to reset our password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="todoApp/reset_password_form.html"), name='password_reset_confirm'),
    #4 Shows a success message that our password was changed
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="todoApp/reset_password_complete.html"), name='password_reset_complete'),
]