# Minha API

<p allign=justify>

Este projeto foi idealizado para prover uma página web onde um operador de um vertiport possa gerenciar a lista de passageiros
confirmados para um voo de eVTOL (Veículo Elétrico que pousa e decola na vertical).

O projeto do MVP foi desenvolvido de forma desacoplada, ou seja, com o back-end e o fron-end implementados separadamente em
repositórios distintos.

Em relação ao back-end e front-end, foi utlizada o padrão MVC, conforme abordado em aula onde no back-end é possível identificar o model e o
controller, e no front-end é possível identificar a view. A comunicação entre a view e o controller é realizada utilizando o
padrão API RESTFUL.

A API foi modelada de acordo com os conceitos abordados em aula. Foram definidas interfaces API Restful que possibilita
a troca de informações no formato JSON envolvendo as requisições e respostas no protocolo HTTP.

Em relação ao banco de dados, foi seguida a orientação para a utilização da biblioteca SQLAlchemy e o SQLite.

</p>

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
