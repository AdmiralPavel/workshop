from django.urls import path
from rest_framework.routers import DefaultRouter

from ..views import MasterView, ServiceView, ReviewView, SessionView, MyRegisterFormView, login

app_name = "workshop"
# app_name will help us do a reverse look-up latter.
router = DefaultRouter()
router.register(r'masters', MasterView, basename='user')
router.register(r'reviews', ReviewView, basename='user')
router.register(r'services', ServiceView, basename='user')
router.register(r'sessions', SessionView, basename='user')
urlpatterns = router.urls
urlpatterns.append(path('login/', login))
"""urlpatterns = [
    path('masters/', MasterView.as_view({'get': 'list'})),
    path('masters/<int:pk>', MasterView.as_view({'get': 'retrieve'})),
    path('services/', ServiceView.as_view()),
    path('services/<int:pk>', SingleServiceView.as_view()),
    path('reviews/', ReviewView.as_view()),
    path('reviews/<int:pk>', SingleReviewView.as_view()),
    path('sessions/', SessionView.as_view()),
    path('sessions/<int:pk>', SingleSessionView.as_view()),
]"""
