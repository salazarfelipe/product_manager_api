from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import ProductSerializer, ProductSerializerPost
from ..models import Product


class ProductViewSet(APIView):

    def get(self, request, format=None):

        serializer = ProductSerializer(Product.objects.all(), many=True)

        return Response(dict(status='done', details=serializer.data), status=200)


class ProductViewSetPost(APIView):

    def post(self, request, format=None):
        print(request.data)
        serializer = ProductSerializerPost(data=request.data)
        try:

            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)
