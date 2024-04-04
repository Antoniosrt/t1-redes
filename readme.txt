PARA RODAR A API É NECESSÁRIO SEGUIR OS PASSOS:
1 - pip install "fastapi[all]"
2 - uvicorn api:app --reload

########################################################################## 

As rota de api são:
1 - http://localhost:8000/ -> Rota de boas vindas
2 - http://localhost:8000/get_data -> Rota para pegar os dados para montar o gráfico
3- http://localhost:8000/docs -> Documentação da API
