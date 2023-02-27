from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductVariation
import pandas as pd
from openpyxl import load_workbook


def index(request):
    result = []

    #fetch all products in Product Model
    allProducts = Product.objects.all()
    paginator = Paginator(allProducts, 3) # per page
    page_number = request.GET.get('page') # get the page number from client
    page_obj = paginator.get_page(page_number)


    # Traverse the page object to fetch all the variations, add into a list
    for product in page_obj:
        variation = Product.objects.get(name=product.name).variations.all()
        product_variance = {
            "item": product,
            "variation": variation,
        }
        result.append(product_variance)

    # send data list along with paginator
    context = {
        "data": result,
        'page_obj': page_obj,
    }
    
    return render(request, 'excelperser/homePage.html', context=context)


@csrf_exempt
def addProduct(request):

    if request.method == 'POST' and request.FILES.get('file'):

        file = request.FILES['file']


        if file.content_type not in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            return JsonResponse({'error': 'Invalid file type'})
        if file.size > 2 * 1024 * 1024:
            return JsonResponse({'error': 'File size exceeded'})
        


        try:

            workbook = load_workbook(filename=file)
            sheet_name = workbook.sheetnames[0]
            worksheet = workbook[sheet_name]

            ok = False

            for line in worksheet:

                if not ok:
                    ok = True
                    continue

                name, variation_text, stock = line[0].value, line[1].value, line[2].value 
                products = Product.objects.filter(name=name)

                if products:

                    variation = ProductVariation.objects.filter(product_id = products[0].id, variation_text=variation_text)

                    if variation:
                        variation[0].stock += stock
                        variation[0].save()
                    else:
                        newVariation = ProductVariation(product_id=products[0].id, variation_text=variation_text, stock=stock)
                        newVariation.save()

                else:
                    
                    newProduct = Product(name=name, lowest_price=0)
                    newProduct.save()

                    newVariation = ProductVariation(product_id=newProduct.id, variation_text=variation_text, stock=stock)
                    newVariation.save()
         
            return JsonResponse({'success': True})
        
        except Exception as e:
            return JsonResponse({'error': str(e)})
            
    else:
        return JsonResponse({'error': 'Invalid request'})
