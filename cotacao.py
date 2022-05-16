import requests

url_dolar = 'https://economia.awesomeapi.com.br/all/USD-BRL'
url_euro = 'https://economia.awesomeapi.com.br/all/EUR-BRL'

response_dolar = requests.get(url_dolar)
response_euro = requests.get(url_euro)

print("Bem vindo ao programa de cotação!")
cotacao = input("Digite qual a moeda desejada: \n(EUR) para Euro \n(DOL) para Dólar: ")

if cotacao == "DOL":
  if response_dolar.status_code == 200:
    dolar_value = response_dolar.json()['USD']['low']
    print("O valor do Dólar é R${}".format(dolar_value))
  else:
    print("Erro ao buscar valor do Dólar")
elif cotacao == "EUR":
  if response_euro.status_code == 200:
    euro_value = response_euro.json()['EUR']['low']
    print("O valor do Euro é R${}".format(euro_value))
  else:
    print("Erro ao buscar valor do Euro")
else:
  print("Valor incorreto!")