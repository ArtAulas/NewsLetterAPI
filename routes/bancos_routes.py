from fastapi import APIRouter, Response
from controller.bancos_controller import BancosController
import os
import sqlite3

router=APIRouter(prefix='/Bancos')

@router.get('/listar')
def listar():
    return BancosController.listar()

@router.post('/bancos/criar')
def CriarBanco(nome:str):
    try:
        return BancosController.criar_banco(nome)
    except:
        return Response(content='Erro ao Criar Banco',status_code=500)