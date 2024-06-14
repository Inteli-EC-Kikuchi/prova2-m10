# prova2-m10

Solução proposta para o exercício prático da prova 2 do módulo 10 <br/>
**Aluno: Filipi Enzo Siqueira Kikuchi**

Para rodar o projeto, basta executar os seguintes comandos:

```bash
git clone https://github.com/Inteli-EC-Kikuchi/prova2-m10.git
```

```bash
docker compose up
```

## API

A api possui 5 endpoints:

- GET /blog/: Retorna todos os posts

Exemplo de retorno:
```json
{
    "posts":
    [
        {
            "title": "Post 1",
            "content": "Content 1"
        },
        {
            "title": "Post 2",
            "content": "Content 2"
        }
    ]
}
```

- GET /blog/:id: Retorna um post específico
  
Exemplo de retorno:
```json
{
    "post": 
    {
        "title": "Post 1",
        "content": "Content 1"
    }
}
```

- POST /blog/: Cria um novo post

Exemplo de requisição:
```json
{
    "title": "Jujutsu Kaisen",
    "content": "Cursed Energy"
}
```

Exemplo de retorno:
```json
{
    "status": "success",
}
```

- PUT /blog/:id: Atualiza um post específico

Exemplo de requisição:
```json
{
    "title": "Hunter x Hunter",
    "content": "Nen"
}
```

Exemplo de retorno:
```json
{
    "status": "success",
}
```

- DELETE /blog/:id: Deleta um post específico

Exemplo de retorno:
```json
{
    "status": "success",
}
```

## Docs

O framework FastAPI possui uma interface de documentação automática, que pode ser acessada em http://localhost:8000/api/docs
