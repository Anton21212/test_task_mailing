from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'mailings', views.MailingViewSet, basename='mailings')
router.register(r'clients', views.ClientViewSet, basename='clients')

urlpatterns = router.urls
