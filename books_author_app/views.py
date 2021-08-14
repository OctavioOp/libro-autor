from django.http.response import JsonResponse
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
        title = request.POST['title']
        desc = request.POST['desc']

        libro_nuevo = Book.objects.create(title=title, desc=desc)
        return redirect('/libro')


def add_book_ajax(request):
    title = request.POST['title']
    desc = request.POST['desc']
    libro_nuevo = Book.objects.create(title=title, desc=desc)
    return JsonResponse({'title': title,
                         'desc': desc,
                         'id': libro_nuevo.id})


def autor(request):
    if request.method == 'GET':
        all_author = Author.objects.all()
        context = {
            'autores': all_author
        }
        return render(request, 'autor.html', context)
    else:
        first_name = request.POST['name']
        last_name = request.POST['l_name']
        notes = request.POST['notes']
        autor_nuevo = Author.objects.create(
            first_name=first_name, last_name=last_name, notes=notes)
        autor_nuevo.save()
        return redirect('/autor')


def delete_author(request, num):
    author_id = Author.objects.get(id=num)
    author_id.delete()
    return redirect('/autor')


def delete(request, num):
    book_id = Book.objects.get(id=num)
    book_id.delete()
    return redirect('/libro')


def getBook(request, num):

    bring_book = Book.objects.get(id=num)
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
    return render(request, 'libroView.html', context)


def add_author(request, id_libro):
    id_a = int(request.POST['autor'])
    autor = Author.objects.get(id=id_a)
    book = Book.objects.get(id=id_libro)
    book.authors.add(autor)
    return redirect(f'/view/book/{id_libro}')


def add_book(request, id_autor):
    id_b = request.POST['book']
    book = Book.objects.get(id=id_b)
    autor = Author.objects.get(id=id_autor)
    autor.books.add(book)
    return redirect(f'/view/autor/{id_autor}')


def get_author(request, num):

    bring_author = Author.objects.get(id=num)
    first_name = bring_author.first_name
    last_name = bring_author.last_name
    notes = bring_author.notes
    all_books = bring_author.books.all()
    belong_book = [autor.id for autor in bring_author.books.all()]
    not_book = [x for x in Book.objects.all() if x.id not in belong_book]
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'notes': notes,
        'all_books': all_books,
        'not_book': not_book,
        'id_author': bring_author.id
    }
    return render(request, 'autorView.html', context)


def remove(request, id_autor, id_libro):
    libro = Book.objects.get(id=id_libro)
    autor = Author.objects.get(id=id_autor)
    autor.books.remove(libro)
    return redirect(request.META.get('HTTP_REFERER')
                    )
