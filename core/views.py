from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse # Formato de resposta de erro de página não encontrada
from django.template import loader

from .models import Product

def index(request):
    products = Product.objects.all()

    context = {
        'course': 'Programação Web com Django Framework',
        'outro': 'Django é Massa!',
        'product': products
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    #model = Product.objects.get(id=pk)
    model = get_object_or_404(Product, id=pk)# Direcionando para mensagem de erro caso não haja o produto

    context = {
        'product': model
    }
    return render(request, 'product.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return  HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


