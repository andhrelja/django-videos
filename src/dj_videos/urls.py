from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from videos.views import VideoListView as IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('videos/', include('videos.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
