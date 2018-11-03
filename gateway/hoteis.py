import requests

base_url = 'https://hotels-microsservico.herokuapp.com/hotels/'


def apagar_hotel(codigo):
    url = '{}{}/'.format(base_url, codigo)
    response = requests.delete(url)
    if response.status_code == 204:
        return True
    raise Exception('erro ao apagar hotel')


def atualizar_hotel(codigo, conteudo):
    url = '{}{}/'.format(base_url, codigo)
    response = requests.put(url, json=conteudo)
    if response.status_code == 200:
        return conteudo
    raise Exception('erro ao atualizar hotel')


def buscar_hotel(codigo=None):
    if codigo:
        url = '{}{}/'.format(base_url, codigo)
    else:
        url = base_url
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise Exception('erro ao buscar hotel')


def salvar_hotel(codigo, conteudo):
    url = '{}{}/'.format(base_url, codigo)
    response = requests.post(url, json=conteudo)
    if response.status_code == 201:
        return response.json()
    raise Exception('erro ao salvar hotel')
