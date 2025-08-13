from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Profile Model for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# Author Model for book authors
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Category Model for book categories
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model for books with rental and purchase features
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Price for buying the book
    rent_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Rent price
    is_rented = models.BooleanField(default=False)  # Rent status flag
    rented_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    rent_start_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def is_overdue(self):
        """Check if the book is overdue"""
        if self.return_date and timezone.now() > self.return_date:
            return True
        return False

    def overdue_fine(self):
        """Calculate overdue fine based on days overdue"""
        if self.is_overdue():
            overdue_days = (timezone.now() - self.return_date).days
            return overdue_days * 10  # Fine per day
        return 0

    def rent_duration(self):
        """Calculate the rent duration in days"""
        if self.rent_start_date:
            return (timezone.now() - self.rent_start_date).days
        return 0

# UserLogin Model to track user logins
class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"
