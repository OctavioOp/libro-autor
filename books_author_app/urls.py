from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('libro',views.libro),
    path('delete/<num>',views.delete),
    path('view/book/<num>',views.getBook),
    path('autor',views.autor),
    path('view/autor/<num>',views.get_author),
    path('delete_author/<num>', views.delete_author),
    path('view/addAutor/<id_libro>',views.add_author),
    path('view/addBook/<id_autor>',views.add_book),

]
