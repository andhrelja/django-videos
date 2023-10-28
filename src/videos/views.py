# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import BaseForm
from django.http.response import HttpResponse
from .models import Video
from .forms import VideoModelForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class VideoListView(ListView):
    model = Video


class VideoDetailView(DetailView):
    model = Video


class VideoCreateView(SuccessMessageMixin, CreateView): # LoginRequiredMixin
    model = Video
    form_class = VideoModelForm
    success_message = "Video created successfully"
    
    def form_valid(self, form: BaseForm) -> HttpResponse:
        form.instance.created_by = self.request.user
        return super(VideoCreateView, self).form_valid(form)


class VideoUpdateView(SuccessMessageMixin, UpdateView): # LoginRequiredMixin
    model = Video
    form_class = VideoModelForm
    success_message = "Video updated successfully"
    
    def form_valid(self, form: BaseForm) -> HttpResponse:
        form.instance.created_by = self.request.user
        return super(VideoUpdateView, self).form_valid(form)


class VideoDeleteView(SuccessMessageMixin, DeleteView): # LoginRequiredMixin
    model = Video
    success_message = "Video deleted successfully"
    success_url = "/videos/"