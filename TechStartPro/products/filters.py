import django_filters
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        category = django_filters.MultipleChoiceFilter(choices=Category.objects.all())
        fields = {
            'name': ['icontains', ],
            'description': ['icontains', ],
            'value': ['exact', ],
            'category': ['exact', ],
        }
