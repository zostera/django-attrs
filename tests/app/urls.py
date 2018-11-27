from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # Test app
    path('', views.HomeView.as_view()),
    path('protocol/<int:protocol_pk>/', views.ProtocolDetailView.as_view()),
    path('protocol/<int:protocol_pk>/visit/create/', views.VisitCreateView.as_view()),
    # Admin site
    url(r"^admin/", admin.site.urls)
]