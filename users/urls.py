from django.urls import path

from users.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView
from rest_framework_simplejwt import views as views_simplejwt

urlpatterns = [

    path('', UserListView.as_view(), name='users_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    path('token/', views_simplejwt.TokenObtainPairView.as_view()),
    path('token/refresh/', views_simplejwt.TokenRefreshView.as_view()),

]
