from floc.views import FlocTemplateView

from . import views


class PlayListView(FlocTemplateView):
    template_name = 'plays/play_list.html'
