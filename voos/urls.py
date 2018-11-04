from django.urls import path

from voos import views


urlpatterns = [
    path('', views.VooListar.as_view(), name='voo_listar'),
    path(
        'apagar/<int:pk>',
        views.VooApagar.as_view(),
        name='apagar_voo'
    ),
    path(
        'detalhe/<int:pk>',
        views.VooDetalhe.as_view(),
        name='detalhe_voo'
    ),
    path(
        'novo',
        views.VooNovo.as_view(),
        name='novo_voo'
    ),
    path(
        'atualizar/<int:pk>',
        views.VooAtualizar.as_view(),
        name='atualizar_voo'
    ),

]
