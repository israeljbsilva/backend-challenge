# Back End Challenge

Criar um projeto Django utilizando o TastyPie ou o Django REST framework como interface API REST.


# Ferramenta de Automação:
Este projeto usa o `Makefile` como ferramenta de automação. 


# Ambiente Virtual de Configuração:
Os seguintes comandos instalam e configuram a ferramenta `pyenv` (https://github.com/pyenv/pyenv) usada para criar / gerenciar ambientes virtuais:

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ exec "$SHELL"
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ exec "$SHELL"
```

Depois disso, acesse o diretório do projeto e execute `make all` para recriar o ambiente virtual.

# Testes

## Executa testes no SQLite:
```
$ make test
```

# Convenção de Código:

## Executa as conveções e métricas no código:
```
$ make code-convention
```

# Documentação da API

A documentação da API está disponível no endpoint `/api-docs/`. Para executar solicitações sobre Swagger, é necessário realizer a autenticação.

# Autenticação:
Foi utilizado o JWT como forma de autenticação.

O JWT é adquirido trocando um nome de usuário + senha por um token de acesso.

## Usuário e Senha:
Foi definido como usuário:
```
israel
```
Foi definido como senha:
```
123456
```

## /auth
- Foi criado o endpoint `/auth` para realizar a autenticação;
- No body, deve-se passar as credenciais informadas acima;
- Na resposta, será retornado o "access" (que é o token de autentecação);

## Authorization:
Via Swagger, pode ser inserido o token (access) através do botão `Authorize` (canto superior direito), informando a literaral "`Bearer + token`", conforme exemplo abaixo:
```
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9.Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY
```

Ou via curl:
```
curl http://127.0.0.1:8000/api/v1/person -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9.Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY'
```

## Projeto:

* Criar uma aplicação simples com dois models (podendo ser Teacher e Student, Person e Pet, ou qualquer outra relação entre duas entidades)
* Criar um relacionamento one-to-many do model 1 para com o model 2
* Implementar todos os métodos de API: C/R/U/D 
   Obs: no GET, o model 2 deve retornar sua relação com o model 1 no resultado, como no exemplo abaixo:

```
{
    "objects": [
        {
            "name "Bobby",
            "id": "1",
            "resource_uri": "/api/v1/pet/1/",
            "person": {
                "name": "John",
                "resource_uri": "/api/v1/person/1/",
                "id": "1"
            }
        },
        {
            "name "Lilly",
            "id": "2",
            "resource_uri": "/api/v1/pet/2/",
            "person": {
                "name": "Robert",
                "resource_uri": "/api/v1/person/2/",
                "id": "2"
            }
        }
    ]
}
```
    

* Criar sistema de autenticação simples, por Basic Autentication (Header ou GET), para restringir o acesso aos dados.
* No DELETE do model 1, os registros do model 2 relacionados ao mesmo devem ser excluídos também.


## Publicação:

Publicar no GitHub ou enviar projeto compactado (zip) por email.