from django.urls import path

from clientes import views


urlpatterns = [
    path('', views.ClienteListar.as_view(), name='cliente_listar'),
    path(
        'apagar/<int:pk>',
        views.ClienteApagar.as_view(),
        name='apagar_cliente'
    ),
    path(
        'novo',
        views.ClienteNovo.as_view(),
        name='novo_cliente'
    ),
    path(
        'atualizar/<int:pk>',
        views.ClienteAtualizar.as_view(),
        name='atualizar_cliente'
    ),

]
