from rest_framework.generics import get_object_or_404, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Master, Service, Review, Session
from .serializers import MasterSerializer, ServiceSerializer, ReviewSerializer, SessionSerializer


class SingleMasterView(RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class MasterView(CreateAPIView, ListAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

    def perform_create(self, serializer):
        master = get_object_or_404(Master, id=self.request.data.get('id'))
        return serializer.save(master=master)


class SingleServiceView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceView(CreateAPIView, ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        service = get_object_or_404(Service, id=self.request.data.get('id'))
        return serializer.save(service=service)


class SingleReviewView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewView(CreateAPIView, ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.request.data.get('id'))
        return serializer.save(review=review)


class SingleSessionView(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionView(CreateAPIView, ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def perform_create(self, serializer):
        session = get_object_or_404(Session, id=self.request.data.get('id'))
        return serializer.save(session=session)