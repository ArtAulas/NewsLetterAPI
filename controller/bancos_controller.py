from service.bancos_service import BancosService
import os

caminho_bancos='./DBs/'

class BancosController():
    def listar():
        return BancosService.listar(caminho_bancos)
    
    def criar_banco(nome):
        if not os.path.exists(caminho_bancos):
            os.mkdir(caminho_bancos)
        return BancosService.criar_banco(caminho_bancos,nome)
