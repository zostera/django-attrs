from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView

from .models import Visit, Protocol
from .forms import VisitFormWithAttrs


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["protocols"] = Protocol.objects.all()
        return context


class ProtocolDetailView(DetailView):
    model = Protocol
    template_name = "protocol_detail.html"


class VisitDetailView(DetailView):
    model = Visit
    template_name = "visit_detail.html"


class VisitCreateView(CreateView):
    model = Visit
    template_name = "form.html"
    form_class = VisitFormWithAttrs

    def get_protocol(self):
        return get_object_or_404(Protocol, pk=self.kwargs["pk"])

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["protocol"] = self.get_protocol()
        return form_kwargs


class VisitUpdateView(UpdateView):
    model = Visit
    template_name = "form.html"
    form_class = VisitFormWithAttrs
