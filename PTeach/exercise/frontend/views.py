from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from api.models import *

def index(request):
  context = {

  }
  return render(request, 'index.html', context)
