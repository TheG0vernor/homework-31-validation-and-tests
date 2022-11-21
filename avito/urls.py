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
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
