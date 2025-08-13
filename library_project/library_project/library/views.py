from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Book, Author, Category, UserLogin
from .forms import BookForm, AuthorForm, CategoryForm, ContactForm, RentOrBuyForm, PaymentForm
from django.utils import timezone

# --- Admin check decorator ---
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)


# --- Views ---

# Home page that lists all books
def home(request):
    books = Book.objects.all().select_related('category').prefetch_related('authors')
    return render(request, 'library/home.html', {'books': books})


# Book Detail page
def book_detail(request, book_id):
    book = get_object_or_404(Book.objects.prefetch_related('authors'), pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})


# Add a new book (only admin users can do this)
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form, 'action': 'Add'})


# Edit an existing book (only admin users can do this)
@login_required
@admin_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form, 'action': 'Edit'})


# Delete a book (only admin users can do this)
@login_required
@admin_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('home')


# Add a new author (only admin users can do this)
@login_required
@admin_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_authors')
    else:
        form = AuthorForm()
    return render(request, 'library/author_form.html', {'form': form, 'action': 'Add'})


# Edit an existing author (only admin users can do this)
@login_required
@admin_required
def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('manage_authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'library/author_form.html', {'form': form, 'action': 'Edit'})


# Delete an author (only admin users can do this)
@login_required
@admin_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    return redirect('manage_authors')


# Manage authors (admin only)
@login_required
@admin_required
def manage_authors(request):
    authors = Author.objects.all()
    return render(request, 'library/manage_authors.html', {'authors': authors})


# Add a new category (only admin users can do this)
@login_required
@admin_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')
    else:
        form = CategoryForm()
    return render(request, 'library/category_form.html', {'form': form, 'action': 'Add'})


# Edit an existing category (only admin users can do this)
@login_required
@admin_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'library/category_form.html', {'form': form, 'action': 'Edit'})


# Delete a category (only admin users can do this)
@login_required
@admin_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('manage_categories')


# Manage categories (admin only)
@login_required
@admin_required
def manage_categories(request):
    categories = Category.objects.all()
    return render(request, 'library/manage_categories.html', {'categories': categories})


# Stats page for admin
@login_required
@admin_required
def stats_view(request):
    users = User.objects.all()
    login_data = []

    for user in users:
        logins = UserLogin.objects.filter(user=user).order_by('-login_time')
        login_times = [entry.login_time for entry in logins]
        login_data.append({
            'username': user.username,
            'joined': user.date_joined,
            'last_login': user.last_login,
            'login_count': logins.count(),
            'login_times': login_times
        })

    stats = {
        'books_count': Book.objects.count(),
        'authors_count': Author.objects.count(),
        'categories_count': Category.objects.count(),
        'users_count': users.count(),
        'user_login_data': login_data,
    }
    return render(request, 'library/stats.html', {'stats': stats})


# Contact form page
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Thanks for your message!')
    else:
        form = ContactForm()
    return render(request, 'library/contact.html', {'form': form})


# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})


# Rent or Buy Book Action
@login_required
def book_action(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = RentOrBuyForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            payment_method = form.cleaned_data['payment_method']

            if action == 'buy':
                return redirect('payment', book_id=book.id, action='buy', payment_method=payment_method)

            elif action == 'rent':
                if book.is_rented:
                    return redirect('home')
                else:
                    book.is_rented = True
                    book.rented_by = request.user
                    book.rent_start_date = timezone.now()
                    book.return_date = timezone.now() + timezone.timedelta(days=30)
                    book.save()
                    return redirect('payment', book_id=book.id, action='rent', payment_method=payment_method)

    else:
        form = RentOrBuyForm()

    return render(request, 'library/book_action.html', {'form': form, 'book': book})


# Payment view for Rent/Buy
@login_required
def payment(request, book_id, action, payment_method):
    book = get_object_or_404(Book, pk=book_id)
    if action == 'buy':
        amount = book.price
    else:
        amount = book.rent_price

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            return render(request, 'library/payment_success.html',
                          {'amount': amount, 'payment_method': payment_method, 'action': action})

    else:
        form = PaymentForm(initial={'amount': amount, 'payment_method': payment_method})

    return render(request, 'library/payment.html', {'form': form, 'amount': amount, 'book': book, 'action': action})


# Custom 404 page
def custom_404(request, exception):
    return render(request, 'library/404.html', status=404)
