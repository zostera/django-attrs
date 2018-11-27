from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # Test app
    path("", views.HomeView.as_view(), name="home"),
    path(
        "protocol/<int:pk>/", views.ProtocolDetailView.as_view(), name="protocol_detail"
    ),
    path(
        "protocol/<int:pk>/visit/create/",
        views.VisitCreateView.as_view(),
        name="visit_create",
    ),
    path(
        "visit/<int:pk>/update/", views.VisitUpdateView.as_view(), name="visit_update"
    ),
    path("visit/<int:pk>/", views.VisitDetailView.as_view(), name="visit_detail"),
    # Admin site
    url(r"^admin/", admin.site.urls),
]
