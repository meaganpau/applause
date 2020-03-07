from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from kudos.models import Kudos
from users.models import UserProfile

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get(self, **kwargs):
        context = super().get(**kwargs)
        context['latest_kudos'] = Kudos.objects.all().order_by('-id')[:5]
        return context

class TeamView(TemplateView):
    template_name = 'team.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kudos'] = Kudos.objects.all()
        context['user_profiles'] = UserProfile.objects.all()
        return context