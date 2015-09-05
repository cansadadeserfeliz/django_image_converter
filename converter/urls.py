from django.conf.urls import url
from django.conf.urls import patterns

from .views import ConverterFormView


urlpatterns = patterns(
    '',

    url(
        r'^$',
        ConverterFormView.as_view(template_name='converter/home.html'),
        name='converter_form'
    ),
)