from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book, Author, BookInstance, Genre, Language


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count() # The all() is implied by Default
    num_genres = Genre.objects.all().count()
    books_containing_the = Book.objects.filter(title__contains="the").count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0) # Gets num_visits session key, default to 0 if not been set previously
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_instances':num_instances, 'num_instances_available':num_instances_available, 'num_authors':num_authors,
        'num_genres': num_genres, 'books_containing_the': books_containing_the, 'num_visits':num_visits},
    )

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current username
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class AllLoanedBooksForStaffView(PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing all on loan books- only staff can see
    """
    permission_required = 'catalog.can_mark_returned'
    model = BookInstance
    template_name = 'catalog/bookinstance_list_all_books.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

class BookListView(generic.ListView):
    model = Book
    paginate_by = 4

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
