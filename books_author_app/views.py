from django.shortcuts import redirect, render, HttpResponse
from .models import Book, Author


def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


def libro(request):
    if request.method == 'GET':
        libro = Book.objects.all()
        context = {
            'libro': libro,
        }
        return render(request, 'libro.html', context)
    else:
        book = request.POST['libro']
        desc = request.POST['desc']

        libro_nuevo = Book.objects.create(title=book, desc=desc)
        libro_nuevo.save()
        return redirect('/libro')


def delete(request, num):
    book_id = Book.objects.get(id=num)
    book_id.delete()
    return redirect('/libro')

def getBook(request,num):
    if request.method == 'GET':
        bring_book = Book.objects.get(id= num)
        title = bring_book.title
        desc = bring_book.desc
        id_book = bring_book.id
        authors1 = bring_book.authors.all()
        book_belong = [author.id for author in authors1]
        not_author = [x for x in Author.objects.all() if x.id not in book_belong]
       
        context = {
            'title': title,
            'desc': desc,
            'id_book': id_book,
            'authors': authors1,
            'not_author': not_author
        }
        return render(request,'libroView.html',context)
    else:
        id_a = request.POST['autor']
        autor = Author.objects.get(id = id_a)
        book = Book.objects.get(id = num)
        book.authors.add(autor)
        book.save()
        return redirect ('libroView.html')
