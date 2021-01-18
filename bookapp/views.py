from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    home_title = 'Buy Books - VJABooks.Com'
    book = Book.objects.all()
    cate12 = Category.objects.filter(pk__in=[1,2])
    cat3 = Category.objects.filter(pk__in=[3])
    cat4 = Category.objects.filter(pk__in=[4])
    cat5 = Category.objects.filter(pk__in=[5])
    # # cat = Category.objects.filter(pk=1)
    # for cat in cate:
    # #     print(ct.name)
    # # print(cate.name)
    return render(request, 'index.html', {'book':book,'cate12':cate12,'cat3':cat3,'cat4':cat4,'cat5':cat5,'home_title':home_title})

def bookDetail(request, slug):
    title = 'VJABooks.Com'
    book = Book.objects.get(slug=slug)
    return render(request, 'book-details.html', {'book':book,'title':title})
    