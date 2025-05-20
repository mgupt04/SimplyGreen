from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('book-reservation/', views.book_reservation, name='book_reservation'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('cart/', views.cart, name='cart'),
    path('cart/increase/<int:item_id>/',
         views.increase_cart_item, name='increase_cart_item'),
    path('cart/decrease/<int:item_id>/',
         views.decrease_cart_item, name='decrease_cart_item'),
    path('documentation/', views.documentation, name='documentation'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),  # Add this line
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
