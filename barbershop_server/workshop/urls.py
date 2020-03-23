from django.urls import path
from ..views import MasterView, ServiceView, ReviewView, SessionView

app_name = "workshop"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('masters/', MasterView.as_view()),
    path('masters/<int:pk>', MasterView.as_view()),
    path('services/', ServiceView.as_view()),
    path('services/<int:pk>', ServiceView.as_view()),
    path('reviews/', ReviewView.as_view()),
    path('reviews/<int:pk>', ReviewView.as_view()),
    path('sessions/', SessionView.as_view()),
    path('sessions/<int:pk>', SessionView.as_view()),
]