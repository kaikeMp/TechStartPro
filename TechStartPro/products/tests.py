from django.test import TestCase
from .models import Product, Category

class ProductCategoryTestCase(TestCase):

    def test_product_categories_exist(self):
        """If any product has any category not registered throw an error"""
        results = []
        for product in Product.objects.all():
                for category in product.category:
                    results.append(Category.objects.get(id=category.id))
        self.assertTrue(all([False]),
        msg=str(results))
