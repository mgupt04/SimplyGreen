from django.shortcuts import render, redirect
from .models import MenuItem, CartItem, Reservation, Blog, ContactMessage
from django.contrib import messages


def home(request):
    latest_blogs = Blog.objects.all()[:2]  # Get the 2 most recent blog posts
    return render(request, 'website/home.html', {'latest_blogs': latest_blogs})


def about(request):
    return render(request, 'website/about.html')

def reservation_success(request):
    return render(request, 'website/reservation_success.html')

def reservation(request):
    return render(request, 'website/reservation.html')


def documentation(request):
    return render(request, 'website/documentation.html')


def menu(request):
    category = request.GET.get('category')
    if category:
        items = MenuItem.objects.filter(category=category)
    else:
        items = MenuItem.objects.all()
    return render(request, 'website/menu.html', {'items': items})


def cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.menu_item.price *
                      item.quantity for item in cart_items)
    return render(request, 'website/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, item_id):
    menu_item = MenuItem.objects.get(id=item_id)
    cart_item, created = CartItem.objects.get_or_create(menu_item=menu_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def place_order(request):
    if request.method == 'POST':
        # Clear the cart (order simulation)
        CartItem.objects.all().delete()
        return redirect('home')
    return render(request, 'website/place_order.html')


def book_reservation(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        num_guests = request.POST['num_guests']
        reservation_time = request.POST['reservation_time']
        location = request.POST['location']
        Reservation.objects.create(
            full_name=full_name,
            email=email,
            num_guests=num_guests,
            reservation_time=reservation_time,
            location=location
        )
        return redirect('home')
    return render(request, 'website/reservation.html')


def blog(request):
    blog_posts = Blog.objects.all()
    return render(request, 'website/blog.html', {'blog_posts': blog_posts})


def blog_detail(request, blog_id):
    post = Blog.objects.get(id=blog_id)
    return render(request, 'website/blog_detail.html', {'post': post})


def increase_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def decrease_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            # Save the form data to the database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! It has been saved, and we’ll get back to you soon.')
            return redirect('contact')
        except Exception as e:
            messages.error(request, 'There was an error saving your message. Please try again later.')
            return redirect('contact')

    return render(request, 'website/contact.html')
