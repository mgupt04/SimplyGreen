from django.db import models
from django.utils import timezone


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('appetizers', 'Appetizers'),
        ('soups_salads', 'Soups & Salads'),
        ('mains', 'Mains'),
        ('sides', 'Sides'),
        ('desserts', 'Desserts'),
        ('drinks', 'Drinks'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    calories = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"


class Reservation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    num_guests = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 10)])
    reservation_time = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Reservation for {self.full_name} on {self.reservation_time}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview = models.TextField(max_length=500)
    image = models.ImageField(upload_to='blog_images/')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-submitted_at']

