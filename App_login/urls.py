from django.urls import path
from App_login import views


app_name="App_login"

urlpatterns = [
    path('singup/',views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('update/', views.user_change_profile, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('change_picture/', views.set_profile_pic, name='change_picture'),
    path('update_profile_pic/', views.update_profile_pic, name='update_profile_pic')
]
