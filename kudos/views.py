from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import(
    CreateView
)
from django.urls import reverse
from .forms import KudosForm
from .models import Kudos
from users.models import UserProfile

# Create your views here.
class KudosListView(LoginRequiredMixin, View):
    template_name = "kudos/kudos_list.html"

    def get(self, request, *args, **kwargs):
        queryset = Kudos.objects.all().order_by('-id')
        self.context = { 'object_list': queryset }
        return render(request, self.template_name, self.context)

class KudosCreateView(LoginRequiredMixin, CreateView):
    template_name = "kudos/kudos_create.html"
    form_class = KudosForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sender = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('kudos:kudos-list')