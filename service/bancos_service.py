import os
import sqlite3

class BancosService():

    def listar(caminho):
      return os.listdir(caminho) 

    def criar_banco(caminho,nome):
       caminho_banco=f'{caminho}{nome}.db'
       sqlite3.connect(caminho_banco)
       return caminho_banco