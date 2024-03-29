"""PRJCT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # рассказываем джанге где искать статику и медиа файлы
from django.conf import settings
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('categories', CategoryViewSet)
# router.register('products', ProductViewSet)
#
# django_router = [
#     path('products/', include('products.routes')),
#     path('categories/', include('products.routes.categories'))
# ]

urlpatterns = [
    # path('api/', include(router.urls)),
    # path('django_api/', include(django_router)),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('categories/',include('products.urls.categories'))
#стандартная процедура добавления медиа, описанная в документации для доступа к файлам на лок машине
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
