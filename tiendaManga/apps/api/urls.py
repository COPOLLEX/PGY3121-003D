from django.urls import path, include
from rest_framework import routers
from apps.api import views

router=routers.DefaultRouter()
router.register(r'Product',views.ProductViewSet)

urlpatterns = [
    path('',include(router.urls))
]
