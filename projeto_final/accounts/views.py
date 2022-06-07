from django.shortcuts import render
from django.http import HttpResponseRedirect

from . forms import CadastrarUserEmpresa
from . forms import CadastrarEmpresa

from django.contrib.auth.models import User
from accounts.models import Empresa

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'usuarios/index.html'




def cadastrarEmpresa(request):


        if request.method == "POST":
            form = CadastrarEmpresa(request.POST)
            
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/login/')
        else:
            form = CadastrarEmpresa()
        
        context = {
            'form': form
        }
        
        return render(request, 'registration/cadastroEmpresa.html', context)


def cadastrarUserEmpresa(request):

    if request.method == "POST":
        form = CadastrarUserEmpresa(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/cadastrarEmpresa/')
    else:
        form = CadastrarUserEmpresa()
    
    context = {
        'form': form
    }
    
    return render(request, 'registration/cadastro.html', context)
