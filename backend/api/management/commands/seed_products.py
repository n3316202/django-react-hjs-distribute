from django.core.management.base import BaseCommand
from api.models import Category, Product

# dev_12
class Command(BaseCommand):
    help = "Create 100 dummy Product objects linked to a Category"

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name="더미 카테고리")

        products_to_create = [
            Product(name=f"제품 {i+1}", category=category) for i in range(100)
        ]
        Product.objects.bulk_create(products_to_create)

        self.stdout.write(self.style.SUCCESS("✅ Product 100개 생성 완료!"))