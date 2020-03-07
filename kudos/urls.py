from django.urls import path
from .views import (
    KudosListView,
    KudosCreateView
)

app_name = "kudos"

urlpatterns = [
    path('', KudosListView.as_view(), name="kudos-list"),
    path('create/', KudosCreateView.as_view(), name="kudos-create")
]
