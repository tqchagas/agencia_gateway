import requests

base_url = 'https://vendas-microsservico.herokuapp.com/vendas/'


def apagar_venda(codigo):
    url = '{}{}/'.format(base_url, codigo)
    response = requests.delete(url)
    if response.status_code == 204:
        return True
    raise Exception('erro ao apagar venda')


def buscar_venda(codigo=None):
    if codigo:
        url = '{}{}/'.format(base_url, codigo)
    else:
        url = base_url
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise Exception('erro ao buscar venda')


def salvar_venda(conteudo):
    response = requests.post(base_url, json=conteudo)
    if response.status_code == 201:
        return response.json()
    raise Exception('erro ao salvar venda')
