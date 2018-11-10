import requests

base_url = 'https://voos-microsservico.herokuapp.com'


def apagar_voo(codigo):
    url = '{}/voos/{}/'.format(base_url, codigo)
    response = requests.delete(url)
    if response.status_code == 204:
        return True
    raise Exception('erro ao apagar voo')


def atualizar_voo(codigo, conteudo):
    url = '{}/voos/{}/'.format(base_url, codigo)
    response = requests.put(url, json=conteudo)
    if response.status_code == 200:
        return conteudo
    raise Exception('erro ao atualizar voo')


def buscar_aeroporto():
    url = '{}/aeroportos/'.format(base_url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise Exception('erro ao buscar voo')


def buscar_voo(codigo=None):
    if codigo:
        url = '{}/voos/{}/'.format(base_url, codigo)
    else:
        url = '{}/voos/'.format(base_url, codigo)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise Exception('erro ao buscar voo')


def salvar_voo(conteudo):
    url = '{}/voos/'.format(base_url)
    response = requests.post(url, json=conteudo)
    return response.json()
