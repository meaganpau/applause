from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import(
    CreateView
)
from django.urls import reverse
from .forms import KudosForm
from .models import Kudos
from django.contrib.auth.models import User

# Create your views here.
class KudosListView(LoginRequiredMixin, View):
    template_name = "kudos/kudos_list.html"
    queryset = Kudos.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = { 'object_list': self.get_queryset() }
        return render(request, self.template_name, context)

class KudosCreateView(LoginRequiredMixin, CreateView):
    template_name = "kudos/kudos_create.html"
    form_class = KudosForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sender = User.objects.get(username=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('kudos:kudos-list')