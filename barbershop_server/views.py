from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MasterSerializer, ServiceSerializer
from .models import Master, Service
from rest_framework.generics import get_object_or_404


class MasterView(APIView):
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
        return Response({"success": "Master '{}' created successfully".format(master_saved.title)})

    def put(self, request, pk):
        saved_master = get_object_or_404(Master.objects.all(), pk=pk)
        data = request.data.get('master')
        serializer = MasterSerializer(instance=saved_master, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            master_saved = serializer.save()
        return Response({
            "success": "Master '{}' updated successfully".format(master_saved.title)
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
        return Response({'services': serializer.data})

    def post(self, request):
        article = request.data.get('service')
        serializer = ServiceSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            service_saved = serializer.save()
        return Response({"success": "Service '{}' created successfully".format(service_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Master.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = MasterSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(article_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        master = get_object_or_404(Master.objects.all(), pk=pk)
        master.delete()
        return Response({
            "message": "Master with id `{}` has been deleted.".format(pk)
        }, status=204)
