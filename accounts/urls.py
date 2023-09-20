from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login_view, name="login_page"),
    path('register/', views.register_view, name="register_page"),
    path('logout/', views.logout_view, name='logout_user'),
    path('dashboard/', views.dashboard, name="dashboard")
]
