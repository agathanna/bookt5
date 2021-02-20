from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book
from django.db.models import Q
from django.http import  HttpResponse, HttpResponseRedirect, JsonResponse

def index(request): 
    entries = Book.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Book.objects.filter(Q(plot_summary__icontains=search))

        context = {
            'result': results
        }
        return render(request, 'entries/index.html', context)
    
    context = {'entries': entries}

    return render (request,  'entries/index.html', context ) 

def add(request):

    return render (request, 'entries/add.html' )

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'entries/upload.html')

def plot_summary_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data = Book.objects.using('legacy').filter(plot_summary__startswith=q).values_list('plot_summary',flat=True)
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")
   
def autocomplete(request):
    if 'term' in request.GET:
        qs = Book.objects.filter(plot_summary__icontains= request.GET.get('term'))
        book_title = list()
        for book in qs:(book.book_title)
        return JsonResponse(book_title, safe=False)
    return render (request, 'entries/index.html')

def search(request):

    if request.method == 'GET':
        search= request.GET.get('search', '')
        post=Book.objects.all().filter(plot_summary="Search")

    return render (request, 'entries/search.html', {'post': post})



