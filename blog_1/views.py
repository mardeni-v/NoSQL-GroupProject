from django.views.generic import ListView, TemplateView
from django.core.paginator import Paginator
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 5


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ImputPageView(TemplateView):
    template_name = 'imput.html'

