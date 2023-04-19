from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from product.models import Product


class ProductListView(ListView):
    model = Product
    #'product_list.html', {product_list' : Product.objets.all()}


class ProductDetailView(DetailView):
    model = Product
    #'product_detail.html' {'product': Product.objects.get(pk=pk)} pk = 'primary key'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']  #'__all__'
    template_name_suffix = '_create'    #product_form.html -> product_create.html
    success_url = reverse_lazy('product:list')  #추가 성공하면, 이동할 url 이름

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price']
    template_name_suffix = '_update'  #product_form.html -> product_update.html
    # 일반적으로 성공하면 detail로 간다
    # success_url = reverse_lazy('product:list') #수정 성공하면, 이동할 url 이름
