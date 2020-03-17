from django.shortcuts import render
from django.http import HttpResponse
import os
import json
import config

# Create your views here.

def index(request):
    photos_list = os.listdir(os.path.join(config.ARCHIVE_PATH, 'photos'))
    return render(request, 'main/index.html', { 'list': photos_list })
