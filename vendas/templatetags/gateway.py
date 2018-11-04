import gateway

from django import template

register = template.Library()


@register.filter
def dados_cliente(id_cliente):
    cliente = gateway.clientes.buscar_cliente(id_cliente)
    return '#{} - {}'.format(cliente['id'], cliente['nome'])


@register.filter
def dados_hotel(id_hotel):
    hotel = gateway.hoteis.buscar_hotel(id_hotel)
    return '{} R$ {}/dia'.format(hotel['nome'], hotel['valor_diaria'])


@register.filter
def dados_voo(id_voo):
    voo = gateway.voos.buscar_voo(id_voo)
    return 'Voo: {} -- {} <{}> - {} <{}>'.format(
        voo['numero'], voo['origem'], voo['destino'],
        voo['partida'], voo['chegada']
    )
