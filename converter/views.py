import uuid

from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from djcelery.models import TaskState
from celery import states

from .forms import ImageForm
from .tasks import task_convert_image


class ConverterFormView(FormView):
    form_class = ImageForm
    template_name = 'converter/home.html'
    success_url = reverse_lazy('converter:converter_form')

    def get_context_data(self, **kwargs):
        context = super(ConverterFormView, self).get_context_data(**kwargs)
        context['task_states'] = states
        context['tasks'] = TaskState.objects.filter(
            name='converter.tasks.task_convert_image',
        )
        return context

    def form_valid(self, form):
        image = form.cleaned_data['image']
        filename = '{0}.jpg'.format(uuid.uuid4())
        task_id = task_convert_image.delay(image.file, filename)

        messages.success(
            self.request,
            'We are converting your image. Task #: {0}'.format(task_id)
        )

        return super(ConverterFormView, self).form_valid(form)