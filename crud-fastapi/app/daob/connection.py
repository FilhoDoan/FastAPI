''' Conexão com o banco SQLALCHEMY
-----------------------------------------------------------------------------------------------
'''


from decouple import config                 ##importacao das variaveis de ambiente 
from sqlalchemy import create_engine        ##criar a engine pra fazer connection de banco de dados em si
from sqlalchemy.orm import sessionmaker     ##ferramenta para conectarmos com o banco (padrao do SQLALCHEMY)

DB_URL = config('DB_URL')                   ##pegar a URL que esta na variavel de ambiente 

engine = create_engine(DB_URL, pool_pre_ping=True) ##pool_pre_ping para ver se esta funcionado o banco antes de fazer qualquer query 
Session = sessionmaker(bind=engine)                ## bindar a session assim garantindo que esta tudo conectado 


