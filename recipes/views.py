from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Nayara Bernardo'
    })

def recipe(request, id):
    return render(request, 'recipes/pages/repice-view.html', context={
        'name': 'Nayara',
    })


#teste HUPDATA
def teste(request):
    return render(request, 'recipes/pages/teste.html')

def atualizar_serie(request):
    return render(request, 'recipes/pages/atualizar_serie.html')





