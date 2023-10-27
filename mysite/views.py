from django.shortcuts import render

# from django.http import HttpResponse
from django.shortcuts import render
from .models import MainContent

def index(request):
    # return HttpResponse("Hello world")
    content_list = MainContent.objects.order_by('-pub_date') #'-pub_date': 역순
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)