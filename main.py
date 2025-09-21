from fastapi import FastAPI
from routes.bancos_routes import router

app=FastAPI()

@app.get('/helloworld')
def HelloWorld():
    return 'Hello World'

app.include_router(router)

if __name__=='__main__':
    import uvicorn
    uvicorn.run('main:app',host='localhost',port=8003,reload=True)