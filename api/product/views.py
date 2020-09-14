from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Category

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = ProductSerializer