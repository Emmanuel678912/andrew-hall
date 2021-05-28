from django.shortcuts import render

# Create your views here.
def input_page(request):

    context = {}
    return render(request, 'input-page.html', context)

def generate_page(request):

    context = {}

    return render(request, 'generate-page.html', context)

def view_tables(request):

    context = {}

    return render(request, 'view-tables.html', context)

