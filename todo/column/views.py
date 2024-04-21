from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ColumnSerializer
from .models import Column


class ColumnCreateAPIView(APIView):

    def get(self, request):
        columns = Column.objects.all()

        return Response({'data': ColumnSerializer(columns, many=True).data})

    def post(self, request):
        serializer = ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method put nor allowed'})

        try:
            instance = Column.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Objects not found'})

        return Response({f"Item {pk}": "deleted"})
