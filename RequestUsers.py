# Importar as bibliotecas necessárias
import requests
import json
import os

# Definir as variáveis de configuração
#tenant_id = "seu_id_do_tenant"
tenant_id = os.getenv("TENANT_ID")

#client_id = "seu_id_do_client"
client_id = os.getenv("CLIENT_ID")

#client_secret = "seu_secret_do_client"
client_secret = os.getenv("CLIENT_SECRET")

scope = "https://graph.microsoft.com/.default"

#group_id = "seu_id_do_grupo_dinamico"
group_id = os.getenv("GROUP_ID")

# Obter o token de acesso do Azure AD usando o service principal
url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": scope,
    "grant_type": "client_credentials"
}
response = requests.post(url, data=data)
token = response.json().get("access_token")
#print(token)

# Usar o token de acesso para consultar os usuários do grupo dinâmico no Microsoft Graph
headers = {
    "Authorization": f"Bearer {token}"
}
url = f"https://graph.microsoft.com/v1.0/groups/{group_id}/members"
response = requests.get(url, headers=headers)
users = response.json().get("value")

# Salvar os usuários em um arquivo user.json na raiz do script
with open("data/user.json", "w") as file:
    json.dump(users, file, indent=4)
