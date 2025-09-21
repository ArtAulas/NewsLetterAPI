from fastapi import FastAPI, Response
from routes.bancos_routes import router
import sqlite3
import os

app=FastAPI()

@app.get('/helloworld')
def HelloWorld():
    return 'Hello World'

app.include_router(router)

if __name__=='__main__':
    import uvicorn
    uvicorn.run('main:app',host='localhost',port=8003,reload=True)