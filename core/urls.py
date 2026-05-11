from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from tasks.views import TaskViewSet
from accounts.views import (
    RegisterView,
    EmailTokenObtainPairView,
    CurrentUserView,
)

router = routers.DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),

    path("api/register/", RegisterView.as_view()),
    path("api/token/", EmailTokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/me/", CurrentUserView.as_view()),
]