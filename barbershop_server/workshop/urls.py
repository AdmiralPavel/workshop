from django.urls import path

from ..views import MasterView, ServiceView, ReviewView, SessionView, SingleMasterView, SingleServiceView, \
    SingleReviewView, SingleSessionView

app_name = "workshop"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('masters/', MasterView.as_view()),
    path('masters/<int:pk>', SingleMasterView.as_view()),
    path('services/', ServiceView.as_view()),
    path('services/<int:pk>', SingleServiceView.as_view()),
    path('reviews/', ReviewView.as_view()),
    path('reviews/<int:pk>', SingleReviewView.as_view()),
    path('sessions/', SessionView.as_view()),
    path('sessions/<int:pk>', SingleSessionView.as_view()),
]
