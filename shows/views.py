from floc.views import FlocTemplateView

from .models import Show


class ShowTemplateView(FlocTemplateView):
    template_name = 'shows/show_list.html'

    def dispatch(self, request, *args, **kwargs):
        self.show_all = True if request.GET.get('all', False) else False

        return super().dispatch(request, *args, **kwargs)

    def get_past_shows(self):
        if self.show_all:
            return Show.objects.past()
        else:
            return Show.objects.past()[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'upcoming_shows': Show.objects.upcoming(),
            'past_shows': self.get_past_shows(),
            'show_all': self.show_all,
        })

        return context
