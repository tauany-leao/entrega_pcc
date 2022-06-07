#from typing_extensions import Required
#from pickle import TRUE
#from venv import create
from django.db import models
from django.contrib.auth import get_user_model

cursos = (
    ('Técnico em Informática para Internet','Técnico em informática para Internet'),
    ('Técnico em Agropecuaria','Técnico em Agropecuaria'),
    ('Técnico em Agroindustria','Técnico em Agroindustria')
)

class Postagem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    titulo = models.CharField(max_length = 100)
    descricao= models.TextField()
    imagem = models.ImageField(blank = True) 
    cursos = models.CharField(
        max_length= 50,
        choices = cursos,
    )
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    def get_cursos_display(self):
        return '3'

    def __str__(self):
        return self.titulo
    def __str__(self):
        return self.descricao
    def __str__(self):
        return self.imagem
    def __str__(self):
        return self.cursos
    def __str__(self):
        return self.created_at
    def __srt__(self):
        return self.updated_at

  


    