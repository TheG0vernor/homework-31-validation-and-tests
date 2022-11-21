from django.urls import path

from users.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView
from rest_framework_simplejwt import views as views_simplejwt
from rest_framework.authtoken import views as views_authtoken

urlpatterns = [

    path('', UserListView.as_view(), name='users_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    # authentication:
    path('login/', views_authtoken.ObtainAuthToken.as_view()),
    path('token/', views_simplejwt.TokenObtainPairView.as_view()),
    path('token/refresh/', views_simplejwt.TokenRefreshView.as_view()),

]
