from fastapi  import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix = '/grupo',
    tags = ['Grupo']
)

Grupos = list()
@router.post('/criar', response_class= JSONResponse )
def criar(nome_Grupo: str, qtd: int): 
    Grupos.append((nome_Grupo, qtd))
    return Grupos