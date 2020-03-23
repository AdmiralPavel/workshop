from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MasterSerializer, ServiceSerializer, ReviewSerializer, SessionSerializer
from .models import Master, Service, Review, Session
from rest_framework.generics import get_object_or_404, GenericAPIView


class MasterView(ListModelMixin, GenericAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

    def get(self, request, pk=None):
        if pk is not None:
            master = get_object_or_404(Master.objects.all(), pk=pk)
            serializer = MasterSerializer(master, many=False)
            return Response({'master': serializer.data})
        else:
            masters = Master.objects.all()
            serializer = MasterSerializer(masters, many=True)
            return Response({"masters": serializer.data})

    def post(self, request):
        master = request.data.get('master')
        serializer = MasterSerializer(data=master)
        if serializer.is_valid(raise_exception=True):
            master_saved = serializer.save()
        return Response({"success": "Master '{}' created successfully".format(master_saved.name)})

    def put(self, request, pk):
        saved_master = get_object_or_404(Master.objects.all(), pk=pk)
        data = request.data.get('master')
        serializer = MasterSerializer(instance=saved_master, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            master_saved = serializer.save()
        return Response({
            "success": "Master '{}' updated successfully".format(master_saved.name)
        })

    def delete(self, request, pk):
        # Get object with this pk
        master = get_object_or_404(Master.objects.all(), pk=pk)
        master.delete()
        return Response({
            "message": "Master with id `{}` has been deleted.".format(pk)
        }, status=204)


class ServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        service = request.data.get('service')
        serializer = ServiceSerializer(data=service)
        if serializer.is_valid(raise_exception=True):
            service_saved = serializer.save()
        return Response({"success": "Service '{}' created successfully".format(service_saved.name)})

    def put(self, request, pk):
        saved_service = get_object_or_404(Service.objects.all(), pk=pk)
        data = request.data.get('service')
        serializer = ServiceSerializer(instance=saved_service, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            service_saved = serializer.save()
        return Response({
            "success": "Service '{}' updated successfully".format(service_saved.name)
        })

    def delete(self, request, pk):
        # Get object with this pk
        service = get_object_or_404(Service.objects.all(), pk=pk)
        service.delete()
        return Response({
            "message": "Service with id `{}` has been deleted.".format(pk)
        }, status=204)


class ReviewView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        review = request.data.get('review')
        serializer = ReviewSerializer(data=review)
        if serializer.is_valid(raise_exception=True):
            review_saved = serializer.save()
        return Response({"success": "Review '{}' created successfully".format(review_saved.name)})

    def put(self, request, pk):
        saved_review = get_object_or_404(Review.objects.all(), pk=pk)
        data = request.data.get('review')
        serializer = ReviewSerializer(instance=saved_review, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            review_saved = serializer.save()
        return Response({
            "success": "Review '{}' updated successfully".format(review_saved.name)
        })

    def delete(self, request, pk):
        # Get object with this pk
        review = get_object_or_404(Review.objects.all(), pk=pk)
        review.delete()
        return Response({
            "message": "Review with id `{}` has been deleted.".format(pk)
        }, status=204)

class SessionView(APIView):
    def get(self, request):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request):
        session = request.data.get('session')
        serializer = SessionSerializer(data=session)
        if serializer.is_valid(raise_exception=True):
            session_saved = serializer.save()
        return Response({"success": "Session '{}' created successfully".format(session_saved.name)})

    def put(self, request, pk):
        saved_session = get_object_or_404(Session.objects.all(), pk=pk)
        data = request.data.get('session')
        serializer = SessionSerializer(instance=saved_session, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            session_saved = serializer.save()
        return Response({
            "success": "Session '{}' updated successfully".format(session_saved.name)
        })

    def delete(self, request, pk):
        # Get object with this pk
        session = get_object_or_404(Session.objects.all(), pk=pk)
        session.delete()
        return Response({
            "message": "Session with id `{}` has been deleted.".format(pk)
        }, status=204)