from fastapi import FastAPI
from fastapi.responses import JSONResponse
from router.router import router as rotas
from starlette.routing import request_response
app = FastAPI()

""" 
    Post = envia dados
    Get = requisita dados 
    Delete = Deleta dados
    
 """
@app.middleware("http")
def middleware(request, call_next):
    print(request)
    response = call_next(request)
    return response 

Dados = list()

@app.post('/DadosPost',response_class = JSONResponse)
def envia_Dados(nome: str, sobreNome:str):
    Dados.append((nome, sobreNome))
    return{"Msg" : "Cadastro Feito"}

@app.get('/DadosGet', response_class= JSONResponse)
def recebe_Dados():
    return Dados  

app.include_router(rotas)