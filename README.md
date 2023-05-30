# Script Python para consultar usuários do grupo dinâmico no Microsoft Graph

Este é um script Python que usa a API do Microsoft Graph para consultar os usuários de um grupo dinâmico no Azure AD e salvar os resultados em um arquivo JSON.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas requests e msal
- Docker e docker-compose
- Uma conta do Azure AD com permissões para acessar o Microsoft Graph
- Um service principal no Azure AD com as permissões necessárias para ler os grupos e os usuários
- Um grupo dinâmico no Azure AD com alguns usuários atribuídos

## Configuração

- Clone este repositório ou faça o download do script.py e do docker-compose.yaml
- Crie um arquivo .env na mesma pasta do docker-compose.yaml com as seguintes variáveis de ambiente:

```text
TENANT_ID=seu_id_do_tenant
CLIENT_ID=seu_id_do_client
CLIENT_SECRET=seu_secret_do_client
GROUP_ID=seu_id_do_grupo_dinamico
```

- Substitua os valores das variáveis de ambiente pelos seus respectivos valores obtidos no portal do Azure
- Crie uma pasta chamada data na mesma pasta do docker-compose.yaml

## Execução

- Abra um terminal na pasta onde estão os arquivos e execute o seguinte comando:

```bash
docker-compose up --build
```

- Isso irá construir a imagem docker, iniciar o contêiner e executar o script python
- O script irá obter um token de acesso do Azure AD usando o service principal e as credenciais fornecidas
- O script irá fazer uma requisição GET para o endpoint do Microsoft Graph para obter os usuários do grupo dinâmico especificado
- O script irá salvar os usuários em um arquivo JSON chamado users.json na pasta data

## Saída

- Você pode verificar se o script funcionou verificando o terminal e o arquivo users.json na pasta data
- O terminal deve mostrar algo como:

```text
Creating network "script_default" with the default driver
Building app
Step 1/8 : FROM python:3.8
 ---> 7f5b6ccd03e9
Step 2/8 : WORKDIR /app
 ---> Using cache
 ---> 8a9f25d2c0e9
Step 3/8 : COPY script.py .
 ---> Using cache
 ---> 0c5d2a288f25
Step 4/8 : RUN pip install requests msal
 ---> Using cache
 ---> 6c8e6f2f1b1c
Step 5/8 : ARG TENANT_ID
 ---> Using cache
 ---> c0f7d6a59832
Step 6/8 : ARG CLIENT_ID
 ---> Using cache
 ---> f0b1dcb6a14c
Step 7/8 : ARG CLIENT_SECRET
 ---> Using cache
 ---> 9d4cfb98c3bc
Step 8/8 : ARG GROUP_ID
 ---> Using cache
 ---> a1a5e137f382

Successfully built a1a5e137f382
Successfully tagged script_app:latest
Creating script_app_1 ... done
Attaching to script_app_1
app_1  | Obtendo token de acesso...
app_1  | Token obtido com sucesso!
app_1  | Fazendo requisição para o Microsoft Graph...
app_1  | Requisição feita com sucesso!
app_1  | Salvando usuários em users.json...
app_1  | Usuários salvos com sucesso!
script_app_1 exited with code 0

```

- O arquivo users.json deve ter um conteúdo como:

```json
[
    {
        "id": "11111111-1111-1111-1111-111111111111",
        "displayName": "Alice",
        "mail": "alice@contoso.com"
    },
    {
        "id": "22222222-2222-2222-2222-222222222222",
        "displayName": "Bob",
        "mail": "bob@contoso.com"
    },
    {
        "id": "33333333-3333-3333-3333-333333333333",
        "displayName": "Charlie",
        "mail": "charlie@contoso.com"
    }
]
```
