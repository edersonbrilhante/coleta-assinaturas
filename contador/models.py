from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=2)

    def __unicode__(self):
        return '%s - %s' % (self.sigla, self.nome)

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    uf = models.ForeignKey(Estado)

    def __unicode__(self):
        return  '%s - %s' % (self.nome, self.uf)

class Secao(models.Model):    
    numero = models.CharField(max_length=5)

    def __unicode__(self):
        return self.numero

class Zona(models.Model):
    zona = models.CharField(max_length=3)
    cidade = models.ForeignKey(Cidade)
    secoes = models.ManyToManyField(Secao)

    def __unicode__(self):
        return '%s - %s' % (self.zona, self.cidade)

class Coleta(models.Model):
    responsavel_coleta = models.ForeignKey(User, related_name='responsavel_coleta')
    local_coleta = models.ForeignKey(Cidade, related_name='local_coleta')
    zona = models.ForeignKey(Zona)
    quantidade_coletada = models.IntegerField()
    local_atual = models.ForeignKey(Cidade, related_name='local_atual')
    responsavel_atual = models.ForeignKey(User, related_name='responsavel_atual')
    enviado_cartorio = models.BooleanField(default=False)
    quantidade_validada = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return '%s - %s - %s' % (self.responsavel_atual, self.local_atual, str(self.quantidade_coletada))


