from django.test import TestCase
from django.db import reset_queries, connection
from api.models import Product

class NPlusOneTest(TestCase):

    def setUp(self):
        from api.models import Category
        cat = Category.objects.create(name="전자제품")
        for i in range(10):
            Product.objects.create(name=f"제품{i}", category=cat)

    def test_n_plus_one(self):
        from pprint import pprint

        connection.use_debug_cursor = True

        reset_queries()
        products = list(Product.objects.all())  # 쿼리 발생 시킴
        for product in products:
            _ = product.category.name

        pprint(connection.queries)
        print(f"\n❗쿼리 수: {len(connection.queries)}")
        self.assertTrue(len(connection.queries) > 1)
