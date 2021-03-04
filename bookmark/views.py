from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import *

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = reverse_lazy('bookmark:list')