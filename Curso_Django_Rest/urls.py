"""Curso_Django_Rest URL Configuration

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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from tourist_spot.api.viewsets import TouristSpotViewSet
from attractions.api.viewsets import AttractionViewSet
from adresses.api.viewsets import AddressViewSet
from comments.api.viewsets import CommentViewSet
from assessments.api.viewsets import AssessmentViewSet


router = routers.DefaultRouter()
router.register(r'pontoturistico', TouristSpotViewSet)
router.register(r'atracoes', AttractionViewSet)
router.register(r'enderecos', AddressViewSet)
router.register(r'comentarios', CommentViewSet)
router.register(r'avaliacoes', AssessmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
