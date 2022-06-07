from multiprocessing import context
from multiprocessing.dummy import current_process
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Postagem
from django.db import models
from .forms import PostForm

from django.contrib.auth.decorators import login_required

@login_required
def publicacoes(request):
    postagens = Postagem.objects.all().order_by('-created_at').filter(user = request.user)
    
    return render(request,'post/listar.html',{'postagens': postagens})

@login_required
def excluir(request, postagem_id):
       
    Postagem.objects.get(pk=postagem_id).delete()
    
    return HttpResponseRedirect("/post")

@login_required
def criar(request):
  
    if request.method == "POST":
        form = PostForm(request.POST)
    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/post")

    else:
        form = PostForm()
    
    return render(request, 'post/criar.html', {'form': form})

@login_required
def editar(request, postagem_id):

    postagem= Postagem.objects.get(pk=postagem_id)
    
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=postagem)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/post")
    else:
        form = PostForm(instance=postagem)
    context = {
        'form': form,
        'postagem_id': postagem_id
    }
    
    return render(request, 'post/editar.html', context)

@login_required
def feed(request, cursos):
    
    for postagens in cursos:
        if cursos == cursos:
            postagens = Postagem.objects.filter(cursos=cursos).values('titulo', 'descricao', 'cursos')
            #a = Postagem.get_cursos_display()
            return render(request, 'post/feed.html', {'postagens': postagens, 'cursos':cursos}) 
 
    return render(request, 'post/editar.html', {'postagens':postagens, 'cursos': cursos})  