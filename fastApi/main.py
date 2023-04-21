from fastapi import FastAPI

app = FastAPI()

Info = {
    1 : {"Nome" : "Doan", "Idade" : 20, "Curso" : "Software"},
    2 : {"Nome" : "TonyStark", "Idade" : 40, "Curso" : "Mecatronica"},
    3 : {"Nome" : "Neymar", "Idade" : 31, "Curso" : "Educação Fisica"},

}
#Caminho principal
@app.get("/")

def home():
    return {"Pessoas cadastradas" :len(Info) }
#Nomes dos Usuarios
@app.get("/Info/{id_Nome}")

def NumeroId(id_Nome : int):
    return Info[id_Nome]