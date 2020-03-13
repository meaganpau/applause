from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from kudos.models import Kudos
from users.models import UserProfile

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        userQuery = UserProfile.objects.get(user=request.user)
        kudosQuery = Kudos.objects.select_related('sender__userprofile').order_by('-id')[:5]
        self.context = { 
            'latest_kudos': kudosQuery,   
            'user_profile': userQuery
        }
        return render(request, self.template_name, self.context)

class TeamView(TemplateView):
    template_name = 'team.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kudos'] = Kudos.objects.all()
        context['user_profiles'] = UserProfile.objects.all()
        return context