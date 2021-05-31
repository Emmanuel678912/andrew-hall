from django.shortcuts import render
from .models import *

# Create your views here.
def input_page(request):
    if request.method == 'POST':
        first_octet = request.POST.get('first')
        second_octet = request.POST.get('second')
        third_octet = request.POST.get('third')
        fourth_octet = request.POST.get('fourth')
        subnet_mask = request.POST.get('subnet-mask')

        loop_count = 0

        third_octet_count = 0 

        fourth_octet_count = 0 
        for i in range(256):
            loop_count += 1
            if loop_count < 129:
                table, created = TableD.objects.get_or_create(
                    first_octet=first_octet,
                    second_octet=second_octet,
                    third_octet=third_octet,
                    fourth_octet=str(int(fourth_octet) + int(i)),
                    subnet_mask=subnet_mask
                )

            else:
                third_octet_count += 1
                
                table, created = TableD.objects.get_or_create(
                first_octet=first_octet,
                second_octet=second_octet,
                third_octet=str(int(third_octet) + third_octet_count),
                fourth_octet=str(int(fourth_octet) + int(i)),
                subnet_mask=subnet_mask
            )

           

            table.save()
        

    context = {}
    return render(request, 'input-page.html', context)

def generate_page(request):

    context = {}

    return render(request, 'generate-page.html', context)

def view_tables(request):

    context = {}

    return render(request, 'view-tables.html', context)

