from django.test import TestCase
from django.db import connection, reset_queries
from api.models import Product, Category
from pprint import pprint

# dev_12 아래의 명령어로 
# python manage.py test api

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

from django.test import TestCase
from django.db import connection, reset_queries
from api.models import Book, Author
from pprint import pprint


# 1. Book 테이블에서 책 5권 조회
#    ┌────────────┐
#    │   Book     │
#    │────────────│
#    │ id | title │
#    └────────────┘
#       ↓

# 2. Book → book_authors(M2M) → Author 조인으로 저자들 가져옴
#    ┌──────────────┐     ┌────────────────────┐     ┌──────────────┐
#    │    Book      │     │  book_authors (M2M)│     │    Author    │
#    │──────────────│     │────────────────────│     │──────────────│
#    │ id           │ --> │ book_id            │ --> │ id           │
#    │ title        │     │ author_id          │     │ name         │
#    └──────────────┘     └────────────────────┘     └──────────────┘

# 결과적으로,
# Book 1 ──────▶ [Author A, Author B]  
# Book 2 ──────▶ [Author C, Author D]  
# ...

class PrefetchRelatedTest(TestCase):

    def setUp(self):
        """책 5권, 각 책마다 저자 2명씩 연결"""
        for i in range(5):
            book = Book.objects.create(title=f"책{i}")
            for j in range(2):
                author = Author.objects.create(name=f"저자{i}-{j}")
                book.authors.add(author)

    # def test_n_plus_one_prefetch(self):
    #     """prefetch_related 없이 N+1 문제 발생 확인"""
    #     connection.use_debug_cursor = True
    #     reset_queries()

    #     with self.assertNumQueries(6):  # 1 (books) + 5 (각 책의 authors.all())
    #         books = list(Book.objects.all())
    #         for book in books:
    #             authors = list(book.authors.all())  # 🔥 N번 추가 쿼리
    #             _ = [a.name for a in authors]

    #     print("\n❗prefetch_related 없이 실행된 쿼리 목록:")
    #     pprint(connection.queries)
    #     print(f"총 쿼리 수: {len(connection.queries)}")

    def test_with_prefetch_related(self):
        """prefetch_related로 N+1 문제 해결"""
        connection.use_debug_cursor = True
        reset_queries()

        with self.assertNumQueries(2):  # 1 (books), 1 (all authors for those books)
            books = list(Book.objects.prefetch_related("authors"))
            for book in books:
                authors = list(book.authors.all())  # 🔥 추가 쿼리 없음
                _ = [a.name for a in authors]

        print("\n✅ prefetch_related 사용 시 실행된 쿼리 목록:")
        pprint(connection.queries)
        print(f"총 쿼리 수: {len(connection.queries)}")


    