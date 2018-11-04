from django.urls import path

from vendas import views


urlpatterns = [
    path('', views.VendaListar.as_view(), name='venda_listar'),
    path(
        'apagar/<int:pk>',
        views.VendaApagar.as_view(),
        name='apagar_venda'
    ),
    path(
        'detalhe/<int:pk>',
        views.VendaDetalhe.as_view(),
        name='detalhe_venda'
    ),
    # path(
    #     'novo',
    #     views.ClienteNovo.as_view(),
    #     name='novo_cliente'
    # ),
    # path(
    #     'atualizar/<int:pk>',
    #     views.ClienteAtualizar.as_view(),
    #     name='atualizar_cliente'
    # ),

]
