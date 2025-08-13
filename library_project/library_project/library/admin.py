from django.contrib import admin
from .models import Book, Author, Category, Profile

# Registering Book model with customization for list display and filters
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'category', 'price', 'rent_price', 'is_rented')
    search_fields = ('title', 'authors__name')  # Searchable by title and author names
    list_filter = ('category', 'publication_date', 'is_rented')  # Filter by category, publication date, and rental status
    ordering = ('-publication_date',)  # Order by publication date descending

# Registering Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)

# Registering Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# Registering Profile model (associated with User)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)  # Search by associated user
    ordering = ('user',)
