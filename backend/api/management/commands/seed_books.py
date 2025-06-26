from django.core.management.base import BaseCommand
from api.models import Book, Author

class Command(BaseCommand):
    help = "📚 Create 5 dummy Book objects, each with 2 Authors (ManyToMany)"

    def handle(self, *args, **options):
        books = []

        for i in range(5):
            book = Book.objects.create(title=f"더미 책 {i+1}")
            for j in range(2):
                author = Author.objects.create(name=f"저자 {i+1}-{j+1}")
                book.authors.add(author)
            books.append(book)

        self.stdout.write(self.style.SUCCESS("✅ Book 5권과 Author 10명 생성 완료!"))
