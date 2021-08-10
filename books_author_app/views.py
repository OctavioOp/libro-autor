from django.shortcuts import redirect, render, HttpResponse
from .models import Book,Author

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

def libro(request):
    if request.method == 'GET':
        libro= Book.objects.all()
        context = {
            'libro': libro,
        }
        return render(request,'libro.html',context)
    else:
        book = request.POST['libro']
        desc = request.POST['desc']

        libro_nuevo = Book.objects.create(title = book, desc = desc)
        return redirect('/libro')



