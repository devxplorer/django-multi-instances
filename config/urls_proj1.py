from django.views.generic import TemplateView

from .urls_common import *


urlpatterns += (
    url(r'^$', TemplateView.as_view(template_name='proj1/index.html')),
)
