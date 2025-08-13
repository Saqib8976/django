from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home & Book Views
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),

    # Author Views
    path('add-author/', views.add_author, name='add_author'),
    path('edit-author/<int:author_id>/', views.edit_author, name='edit_author'),
    path('delete-author/<int:author_id>/', views.delete_author, name='delete_author'),
    path('manage-authors/', views.manage_authors, name='manage_authors'),

    # Category Views
    path('add-category/', views.add_category, name='add_category'),
    path('edit-category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('manage-categories/', views.manage_categories, name='manage_categories'),

    # Stats & Contact
    path('stats/', views.stats_view, name='stats'),
    path('contact/', views.contact_view, name='contact'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='library/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    # Book Actions: Buy/Rent Selector + Payment
    path('book/<int:book_id>/action/', views.book_action, name='book_action'),
    path('book/<int:book_id>/payment/<str:action>/<str:payment_method>/', views.payment, name='payment'),

    # Custom 404 Page
    path('404/', views.custom_404, name='404'),
]
