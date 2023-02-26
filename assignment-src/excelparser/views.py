from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductVariation
import pandas as pd
from openpyxl import load_workbook



def index(request):
    return render(request, 'excelperser/homePage.html')


@csrf_exempt
def addProduct(request):
    
    if request.method == 'POST' and request.FILES.get('file'):
        
        file = request.FILES['file']


        if file.content_type not in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            return JsonResponse({'error': 'Invalid file type'})
        if file.size > 2 * 1024 * 1024:
            return JsonResponse({'error': 'File size exceeded'})
        

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
    else:
        return JsonResponse({'error': 'Invalid request'})