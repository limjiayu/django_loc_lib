from django.urls import path
from . import views

urlpatterns = [

]

# define empty (imported) uslpatterns
# adding our patterns here as we build the application

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'),


]

urlpatterns += [   
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# registration page
urlpatterns += [
    path('register/', views.RegistrationPage, name='user_create'),
    path('register/confirmation/', views.RegistrationPage, name='user_confirmation'),
    ] 

# url pattern: empty string
# view function to be called if the URL pattern is detected: 
# views.index -> index() function in views.py
# name parameter = unique identifier for this particular URL mapping
    # able to "reverse" the mapper
    # creating URL that points to the resource that the mapper is desinged to handle
    # linking home page from any other page
