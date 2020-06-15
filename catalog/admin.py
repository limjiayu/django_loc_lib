from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

class BookInLine(admin.TabularInline):
    model = Book

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    # differentiate them by providing more information
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # field attribute lists those fields that are displayed on the form in order
    # if placed in tuple, will be side by side
    # else would be vertical
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInLine]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
# @admin.register(Book) = admin.site.register
#@admin.register(Book)
#class BookAdmin(admin.ModelAdmin):
    #list_display = ('title', 'author', 'display_genre')

# Adding associated records (book info + info about specific copies on same detail page)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    # viewing both of them on the same page

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')

    # information related to what the book is (name, imprint, id)
    # and when it will be avail (status, due_back)
    # adding these in different sections 
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )



