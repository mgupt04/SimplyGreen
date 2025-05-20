from django.contrib import admin
from .models import MenuItem, CartItem, Reservation, Blog


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image', 'calories')
    save_as = True


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'reservation_time', 'num_guests', 'location')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('date_posted',)
