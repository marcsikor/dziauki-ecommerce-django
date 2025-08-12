from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import PropertyPosting
from .forms import InputForm

def home(request):
    postings = PropertyPosting.objects.all().values()
    # print(postings)
    template = loader.get_template('index.html')
    context =  {
        'postings': postings,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    posting = PropertyPosting.objects.get(postingID = id)
    template = loader.get_template('details.html')
    context =  {
        'posting': posting,
    }
    return HttpResponse(template.render(context, request))

def new_posting(request):
    context = {}
    template = loader.get_template('property_form.html')
    
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = InputForm()
    
    context['form'] = form
    return HttpResponse(template.render(context, request))

def edit_posting(request, id):
    context = {}
    template = loader.get_template('property_form.html')
    posting = PropertyPosting.objects.get(postingID = id)
    
    if request.method == 'POST':
        form = InputForm(request.POST, instance=posting)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = InputForm(instance = posting)
    
    context['form'] = form
    return HttpResponse(template.render(context, request))
        
def login(request): # future login view
    template = loader.get_template('index.html')
    context =  {}
    return HttpResponse(template.render(context, request))

def signup(request): # future signup view
    template = loader.get_template('index.html')
    context =  {}
    return HttpResponse(template.render(context, request))