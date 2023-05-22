'''


'''

from sqlalchemy import Column, String, Integer
from app.daob.base import Base

'''Heranca da Base -> Base ''' 

class user_model(Base):
    __tablename__ = 'user'
    ##Coluna no banco de dados , id na qual tem o tipo Integer | e chave primaria | nao pode ser nula | gerada automaticamente 
    id = Column('id',Integer, primary_key=True , autoincrement= True, nullable=False )
    user_name = Column('user_name', String, nullable=False, unique=True)
    password = Column('password', String,nullable=False)
    cpf = Column('cpf', String,nullable=False )
    
    
    
    
