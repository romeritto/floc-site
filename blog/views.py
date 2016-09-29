from django.views.generic import ListView

from floc.views import FlocContextMixin
from .models import Blogpost


class BlogpostListView(FlocContextMixin, ListView):
    model = Blogpost
