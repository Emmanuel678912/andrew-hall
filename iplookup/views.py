from django.shortcuts import render
from .models import *

# handles the data for input page
def input_page(request):

    # gets the input data from the form
    if request.method == 'POST':
        # gets all input data
        tablea_column2 = request.POST.get('a-column-2')
        tablea_column3 = request.POST.get('a-column-3')

        tableb_column2 = request.POST.get('b-column-2')

        tablec_column2 = request.POST.get('c-column-2')
        tablec_column3 = request.POST.get('c-column-3')
        tablec_column4 = request.POST.get('c-column-4')

        
        first_octet = request.POST.get('first')
        second_octet = request.POST.get('second')
        third_octet = request.POST.get('third')
        fourth_octet = request.POST.get('fourth')
        subnet_mask = request.POST.get('subnet-mask')
        variable = request.POST.get('variable')

        tableg_column2 = request.POST.get('g-column-2')
        tableg_column3 = request.POST.get('g-column-3')

        loop_count = 0

        third_octet_count = 0 

        fourth_octet_count = 2

        # Saves data to Table A
        tablea, created = TableA.objects.get_or_create(
            column2=tablea_column2,
            column3=tablea_column3
        )

        tablea.save()

        # Saves data to Table B
        tableb, created = TableB.objects.get_or_create(
            column2=tableb_column2
        )
        
        tableb.save()

        # Saves data to Table C
        tablec, created = TableC.objects.get_or_create(
            column2=tablec_column2,
            column3=tablec_column3,
            column4=tablec_column4
        )
        
        tablec.save()

        # Saves data to table D
        for i in range(256):
            loop_count += 1

            try:
                table, created = TableD.objects.get_or_create(
                        first_octet=first_octet,
                        second_octet=second_octet,
                        third_octet=third_octet,
                        fourth_octet=str(int(fourth_octet) + loop_count),
                        subnet_mask=subnet_mask
                )

                table.save()

            except:
                break

        # Saves data to table E 
        for i in range(256):
            loop_count += 1
            try:
                if loop_count < 129:
                    table, created = TableE.objects.get_or_create(
                        first_octet=first_octet,
                        second_octet=second_octet,
                        third_octet=third_octet,
                        fourth_octet=fourth_octet,
                        subnet_mask=subnet_mask
                    )

                else:
                    third_octet_count += 1

                    fourth_octet_count += 2
                    
                    table, created = TableE.objects.get_or_create(
                    first_octet=first_octet,
                    second_octet=second_octet,
                    third_octet=str(int(third_octet) + third_octet_count),
                    fourth_octet=str(int(fourth_octet) + fourth_octet_count),
                    subnet_mask=subnet_mask
                )

            
                table.save()

            except:
                break
        
    
        third_octet_count2 = 0

        # Saves data to table F
        for i in range(64):

            try:
            
                table, created = TableF.objects.get_or_create(
                        first_octet=first_octet,
                        second_octet=second_octet,
                        third_octet=str(int(third_octet) + int(third_octet_count2)),
                        fourth_octet=fourth_octet,
                        subnet_mask=subnet_mask,
                        variable=variable
                )

                table.save()

                third_octet_count2 += 4
            
            except:
                break

        # Saves data to table G
        tableg, created = TableG.objects.get_or_create(
            column2=tableg_column2,
            column3=tableg_column3
        )
        
        tableg.save()
        

    context = {}
    return render(request, 'input-page.html', context)

# Handles the logic for the generate page
def generate_page(request):

    # grab data from each table
    tableg = TableG.objects.all()
    tableh = TableH.objects.all()

    tablea = TableA.objects.all()
    tableb = TableA.objects.all()

    # gets the vendor name and host name 
    if request.method == 'POST':
        vendor = request.POST.get('vendor')
        hostname = request.POST.get('host')

        # tableg_vendor = tableg[0].filter(vendor) 

        # print(tableg_vendor) 
        
        # Where TableG_c2_rX = vendorname print TableG_c3_r1 + Hostname   
        for i in tableg:
            if vendor == i.column2:
                print(str(i.column3[0] + hostname))

        # Where TableH_c2_rX = vendorname print TableH_c3_rX + TableA_c2_r1 (string combination)
        for i in tableh:
            if vendor == i.column2:
                print(str(i.column3) + str(tablea[0].column2[0]))
        
        # Where TableH_c2_rX = vendorname print TableH_c4_rX + TableA_c3_r1 (string combination)
        for i in tableh:
            if vendor == i.column2:
                print(str(i.column4) + str(tablea[0].column3[0]))

        # Where TableH_c2_rX = vendorname print TableH_c5_rX + TableB_c2_r1 (string combination)
        for i in tableh:
            if vendor == i.column2:
                print(str(i.column5) + str(tableb[0].column2[0]))


        for i in tableh:
            if vendor == i.column2:
                print(str(i.column5) + str(tableb[0].column2[0]))

    context = {}

    return render(request, 'generate-page.html', context)

def view_tables(request):

    context = {}

    return render(request, 'view-tables.html', context)

