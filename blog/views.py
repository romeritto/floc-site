from django.views.generic import ListView, DetailView

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


class BlogpostDetailView(FlocContextMixin, DetailView):
    model = Blogpost
    context_object_name = 'blogpost'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_blogposts'] =  Blogpost.objects.filter(
                                        pk__gte=self.object.pk-3
                                    ).exclude(pk=self.object.pk)[:3]
        return context