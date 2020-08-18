from django.conf import settings
from django.views.generic.base import TemplateView

class IndexTemplateView(TemplateView):

    def get_template_names(self):
        #return "index.html"
        if  settings.DEBUG:
            #template_name = "index.html"
            template_name = "index-dev.html"
        else:
            template_name = "index.html"
        return template_name
