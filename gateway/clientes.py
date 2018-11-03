import requests

base_url = 'https://clientes-microsservico.herokuapp.com/clientes/'


def apagar_cliente(codigo):
    url = '{}{}/'.format(base_url, codigo)
    response = requests.delete(url)
    if response.status_code == 204:
        return True
    raise Exception('erro ao apagar cliente')


def atualizar_cliente(codigo, conteudo):
    url = '{}{}/'.format(base_url, codigo)
    response = requests.put(url, json=conteudo)
    if response.status_code == 200:
        return conteudo
    raise Exception('erro ao atualizar cliente')


def buscar_cliente(codigo=None):
    if codigo:
        url = '{}{}/'.format(base_url, codigo)
    else:
        url = base_url
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise Exception('erro ao buscar cliente')


def salvar_cliente(conteudo):
    response = requests.post(base_url, json=conteudo)
    if response.status_code == 201:
        return response.json()
    raise Exception('erro ao salvar cliente')
