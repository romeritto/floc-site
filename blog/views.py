from floc.views import FlocTemplateView


class BlogpostListView(FlocTemplateView):
    template_name = 'blog/blogpost_list.html'
