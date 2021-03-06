from django.urls import path
from .views import *

urlpatterns = [
    path('', DownloadsView.as_view(), name='downloads'),
    path('<int:pk>/', DownloadsDeviceView.as_view(), name='downloads_device'),
    path('maintainers/', MaintainerDashboardView.as_view(), name='dashboard'),
    path('maintainers/device/<int:pk>/', DeviceDetailView.as_view(), name='device_detail'),
    path('maintainers/device/<int:pkd>/build/<int:pk>/', BuildDetailView.as_view(), name='build_detail'),
    path('maintainers/device/<int:pkd>/build/<int:pk>/delete/', BuildDeleteView.as_view(), name='build_delete'),
    path('maintainers/device/<int:pk>/upload/', build_upload, name='build_upload'),
    path('maintainers/api/login/', maintainer_api_login, name='maintainer_api_login'),
    path('maintainers/api/device/id/', maintainer_api_device_id, name='maintainer_api_device_id'),
    path('maintainers/api/device/<int:pk>/upload/', maintainer_api_build_upload, name='maintainer_api_build_upload'),
]
