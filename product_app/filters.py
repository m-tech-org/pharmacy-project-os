import django_filters
from product_app.models import product, category


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = product
        fields = ['product_name']

class CategoryFilter(django_filters.FilterSet):
    class Meta: 
        model = category
        fields = ['name']