from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def pestaña(request):
	return render(request, 'miapp/pestaña.html')

def Carreras(request):
	return render(request, 'miapp/Carreras.html')

def CuerpoDocente(request):
	return render(request, 'miapp/CuerpoDocente.html')


