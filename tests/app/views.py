from django.views.generic import CreateView, TemplateView, DetailView

from .models import Visit, Protocol
from .forms import VisitFormWithAttrs


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocols'] = Protocol.objects.all()
        return context


class ProtocolDetailView(DetailView):
    model = Protocol


class VisitCreateView(CreateView):
    model = Visit
    fields = ['name']
    template_name = 'form.html'
    form = VisitFormWithAttrs
