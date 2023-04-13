# Importing necessary modules and views from the same app
from django.urls import path
from .views import ProductListView, ProductDetailView, CheckoutView

# Importing static urls and settings from django conf
from django.conf.urls.static import static
from django.conf import settings

# Define url patterns
urlpatterns = [
    # List view of all products
    path('', ProductListView.as_view(), name='product_list'),
    # Detail view of each product with id as parameter
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # Checkout view for purchasing products
    path('checkout/', CheckoutView.as_view(), name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Serving media files


"""
This code creates the urlpatterns variable which contains a list of URL patterns supported by the Django application. The three URLs defined are mapped to the ProductListView, ProductDetailView, and CheckoutView classes respectively.

The path() function maps a route to a class-based view. It takes two required arguments: the route string and the view class. Optional named arguments can also be passed to specify the view name.

The last line adds support for serving media files. The MEDIA_URL is defined in the settings file along with the MEDIA_ROOT where the actual files reside. The static() function serves files from MEDIA_ROOT on the specified MEDIA_URL.

"""