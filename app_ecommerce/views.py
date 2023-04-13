from django.views.generic import ListView,DetailView,View
from .models import Product
from django.shortcuts import render, redirect

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'



class CheckoutView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        # Add checkout logic here
        return redirect('product_list')
