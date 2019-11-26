import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    ListView, DetailView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy

from django.http import Http404, JsonResponse

# from accounts.mixins import AdminRoleRequired
# from products.forms import ProductForm
from products.models import Product


class ProductJsonListView(ListView):
    model = Product
    paginate_by = 10

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'title': itm.title,
                    'category': str(itm.category) if itm.category else None,
                    'image': itm.image.url,
                    'cost': itm.cost,
                },
                queryset
            )
        )


# Create your views here.
def products(request):
    context = {
        'contacts': [
            'Contact 1',
            'Contact 2',
            'Contact 3',
        ],
        'file':'The card'
    }

    response_string = render_to_string(
        'products/products.html',
        context
    )
    
    return HttpResponse(response_string)

def product_detail(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    context = {'object':obj}
    return render(request, 'products/detail.html', context)

class ProductCreateView(CreateView):
    model = Product
    fields = [
        'title',
        'category',
        'image',
        'snippet',
        'cost',
    ]
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:products')
    login_url = reverse_lazy('accounts:login')

class ProductUpdateView(LoginRequiredMixin, UpdateView): #AdminRoleRequired, 
    model = Product
    fields = [
        'title', 'category', 'image',
        'snippet', 'cost'
    ]
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:list')
    login_url = reverse_lazy('accounts:login')


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:list')
    login_url = reverse_lazy('accounts:login')

    def test_func(self):
        return self.request.user.is_superuser



class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'


def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    success_url = reverse_lazy('main:index')
    
    if request.method == 'POST':
        obj.delete()
        
        return redirect(success_url)

    return render(request, 'products/delete.html', {'obj': obj})


def product_update(request, pk):
    # try:
    #     obj = Product.objects.get(pk=pk)
    # except Exception as err:
    #     raise Http404
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=obj)
    success_url = reverse_lazy('main:index')

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request, 
        'products/update.html',
        {
            'form': form,
            'obj': obj
        }
    )


@login_required(login_url=reverse_lazy('accounts:login'))
def product_create(request):
    form = ProductForm()
    success_url = reverse_lazy('main:index')

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})

def product_list(request):
    # context = {}

    # with open('products/data/products.json', 'r') as file:
    #     context = json.load(file)

    # return render(request, 'products/list.html', context)

    # query = Product.objects.all()

    query = get_list_or_404(Product)
    page = request.GET.get('page')
    paginator = Paginator(query, 10)

    products = paginator.get_page(page)

    return render(request, 'products/list.html', {'products': products})


def product_detail(request, pk):
    # context = {}

    # with open('products/data/products.json', 'r') as file:
    #     context = json.load(file)

    # return render(
    #     request, 
    #     'products/detail.html',
    #     {
    #         'object': context['products'][idx]
    #     } 
    # )

    # obj = Product.objects.get(id=pk)

    obj = get_object_or_404(Product, pk=pk)

    return render(request, 'products/detail.html', {'object': obj})

