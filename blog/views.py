from django.views.generic import ListView

from floc.views import FlocContextMixin
from .models import Blogpost


class BlogpostListView(FlocContextMixin, ListView):
    model = Blogpost
    queryset = Blogpost.objects.select_related(
        'author',
        'author__user',
    ).all()
    paginate_by = 5
    context_object_name = 'blogpost_objects'
