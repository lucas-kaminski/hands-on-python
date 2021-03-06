# -*- coding: utf-8 -*-
"""Arquitetura MVC

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VIRTVHGpevwHxMLV8jPtkY0njesjtPgL
"""

#Divide o código em partes
#View: Interface do código/projeto (usuário vai ver)

#Model: Armazenamento e estrutura dos dados 

#Controller: Lógica do programa

#Usuário envia dados pela view, a controller processa, valida ou invalida.
#Se valida, envia pra model
#Se invalida, devolve pra view

#Camada dal: Layer Data Axis

#No projeto, cria umarqui vo para cada
#model.py, controller.py, dal.py aaa.py

#na model
class Pessoa:
  def __init__(self, nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf

#na dal
#from model import Pessoa

class PessoaDal:
  @classmethod
  def Salvar(cls, pessoa: Pessoa):
    with open("pessoas.txt","w") as arq:
      arq.write(pessoa.nome + "" + pessoa.idade + "" + pessoa.cpf)

  @classmethod
  def Ler(cls):
    nome = "Caio"
    idade = 20
    cpf = str("01715849589")
    return Pessoa(nome, idade, cpf)

p1 = Pessoa("Lucas",20,"0151518")

PessoaDal().Ler(self)