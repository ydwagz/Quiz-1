from django.shortcuts import render

def products(request):
    products = [
        {"name": "Laptop", "price": 2500},
        {"name": "Mouse", "price": 80},
        {"name": "Keyboard", "price": 150},
        {"name": "Monitor", "price": 700},
    ]

    context = {"products": products}


    return render(request,'products.html', context)


def home(request):

    return render(request,'home.html')