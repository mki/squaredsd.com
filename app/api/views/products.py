from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import products as products_serializers

from products.models import Products


class ProductsView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    request_serializer_class = products_serializers.ProductsResponseSerializer
    response_serializer_class = products_serializers.ProductsResponseSerializer

    def get(self, request):
        """
        Products
        ---
        serializer: api.serializers.news.NewsRequestSerializer
        """
        products = Products.objects.all().order_by('id')

        response_serializer = self.response_serializer_class(products, many=True)
        return Response(response_serializer.data)

