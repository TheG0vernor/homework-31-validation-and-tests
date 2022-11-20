"""avito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

from ads import views
from selection.views import SelectionViewSet
from users.views import LocationViewSet

router = routers.SimpleRouter()

router.register('locations', LocationViewSet)
router.register('selection', SelectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('cat/', views.CategoryListView.as_view(), name='category_list'),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('ads/', include('ads.urls')),
    path('users/', include('users.urls')),
    # path('selection/'), include('selection.urls')
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
