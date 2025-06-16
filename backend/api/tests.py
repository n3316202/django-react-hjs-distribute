from django.test import TestCase
from django.db import connection, reset_queries
from api.models import Product, Category
from pprint import pprint


class NPlusOneTest(TestCase):

    def setUp(self):
        """테스트를 위한 카테고리 1개, 제품 10개 생성"""
        category = Category.objects.create(name="전자제품")
        for i in range(10):
            Product.objects.create(name=f"제품{i}", category=category)

    def test_n_plus_one(self):
        connection.use_debug_cursor = True
        reset_queries()

        with self.assertNumQueries(11):  # 1 (product list) + 10 (category 접근)
            products = list(Product.objects.all())
            for product in products:
                _ = product.category.name

        print("\n❗N+1 발생 시 실행된 쿼리 목록:")
        pprint(connection.queries)
        print(f"총 쿼리 수: {len(connection.queries)}")

    def test_select_related(self):
        connection.use_debug_cursor = True
        reset_queries()

        with self.assertNumQueries(1):  # select_related로 JOIN 1회
            products = list(Product.objects.select_related("category"))
            for product in products:
                _ = product.category.name

        print("\n✅ select_related 사용 시 실행된 쿼리 목록:")
        pprint(connection.queries)
        print(f"총 쿼리 수: {len(connection.queries)}")
