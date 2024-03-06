from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<str:username>', views.profile_view, name='profile'),
    path('settings/', views.editProfile, name='edit_profile'),
    path('delete/', views.deleteProfile, name='delete_profile'),
    path("terms/", views.terms, name="terms_conditions"),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_view, name='logout'),
    # path('dashboard/<str:username>', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('wallet/',views.wallet,name='wallet'),
    path('prof/',views.prof,name='prof'),

]