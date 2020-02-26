from django.urls import path
from ..views import MasterView, ServiceView

app_name = "workshop"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('masters/', MasterView.as_view()),
    path('masters/<int:pk>', MasterView.as_view()),
    path('services/', ServiceView.as_view()),
    path('services/<int:pk>', ServiceView.as_view()),
]