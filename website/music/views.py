from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('test')

def detail(request, album_id):
    return HttpResponse('details for album id: ' + str(album_id))