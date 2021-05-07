from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Stroj

def index(request):
    context = {
    }

    return render(request, template_name='stroje.html', context=context)

class StrojList(ListView):
    model = Stroj
    context_object_name = 'stroje_list'
    template_name = 'vypis.html'


class DetailStroj(DetailView):
    model = Stroj
    context_object_name = 'stroj'
    template_name = 'detail.html'

