from django.urls import path
from . import api
from . import views

app_name = "videos"
urlpatterns = [
    path('categories', api.get_categories, name="list-categories"),
    path('', views.VideoListView.as_view(), name="list"),
    path('<int:pk>', views.VideoDetailView.as_view(), name="detail"),
    path('create', views.VideoCreateView.as_view(), name="create"),
    path('<int:pk>/update', views.VideoUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', views.VideoDeleteView.as_view(), name="delete"),
    path('<int:pk>/rate/<str:rating>', views.VideoRateView.as_view(), name="rate"),
]
