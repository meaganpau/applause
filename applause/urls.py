"""applause URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path, include
from django.conf.urls import url
from applause.views import (
    HomePageView,
    DashboardView,
    TeamView
)
from users.views import (
    register,
    user_login,
    user_logout,
    user_profile,
)

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('kudos/', include('kudos.urls')),
    path('register/', register, name="register"),
    path('profile/', user_profile, name="profile"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('team/', TeamView.as_view(), name="team"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
