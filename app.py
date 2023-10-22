
import functools
import requests

# Defina a URL da API que você deseja acessar
url = "https://viacep.com.br/ws/69073420/json/"

# Faça uma solicitação GET para a API
try:
  response = requests.get(url)
except:
  print("erro na execução do comando. Verifique sua url")

else:
    # Verifique se a solicitação foi bem-sucedida (código de resposta 200)
  if response.status_code == 200:
    # A resposta JSON da API pode ser acessada com response.json()
    data = response.json()
    # Agora você pode trabalhar com os dados da API
    print(data)
  else:
    # Se a solicitação falhar, imprima uma mensagem de erro
    print("A solicitação à API falhou. Código de resposta:", response.status_code)




