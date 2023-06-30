from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalsView)
urlpatterns = [
    path('', views.cxcontact, name='Form'),
    path('status/', views.cxstatus, name='Status'),
    path('api/', include(router.urls)),
]
