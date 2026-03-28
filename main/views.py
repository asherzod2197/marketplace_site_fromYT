from django.shortcuts import render
from django.views import View
from prducts.models import Product

# Create your views here.

class IndexView(View):
    def get (request):
        products = Product.objects.all()

        context = {
            "products": products
        }
        return render(request, "index.html", context=context)


