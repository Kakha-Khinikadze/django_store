from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Welcome',
        'username': 'David',
        'products': [
            {'name': 'Houdey', 'price': 6000.00},
            {'name': 'Jacket', 'price': 5000.00},
            {'name': 'Top', 'price': 1020.00},
        ],
        'promotion': True,
        'products_of_promotion':[
            {'name': 'Frog', 'price': 500},
        ]
    }
    return render(request, 'products/test-context.html', context)
