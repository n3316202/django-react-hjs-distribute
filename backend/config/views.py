from django.shortcuts import render
from api.models import Book

#dev_1
def main(request):
    
    books = Book.objects.all()  # N+1 문제 일으키기
    
    #books = Book.objects.prefetch_related('authors')  # N+1 방지
    
    return render(request, 'main.html', {'books': books})
    # return render(request, 'main.html')


