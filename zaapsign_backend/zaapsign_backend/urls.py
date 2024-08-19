from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from companies.views import CompanyViewSet, DocumentViewSet, SignerViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'signers', SignerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
