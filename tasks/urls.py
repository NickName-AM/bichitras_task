from django.urls import path

from rest_framework import routers

from tasks import views

# urls

router = routers.SimpleRouter()

router.register(r"", views.TaskViewSet)

urlpatterns = router.urls