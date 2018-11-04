from django.urls import path

from hoteis import views


urlpatterns = [
    path('', views.HotelListar.as_view(), name='hotel_listar'),
    path(
        'apagar/<int:pk>',
        views.HotelApagar.as_view(),
        name='apagar_hotel'
    ),
    path(
        'detalhe/<int:pk>',
        views.HotelDetalhe.as_view(),
        name='detalhe_hotel'
    ),
    path(
        'novo',
        views.HotelNovo.as_view(),
        name='novo_hotel'
    ),
    path(
        'atualizar/<int:pk>',
        views.HotelAtualizar.as_view(),
        name='atualizar_hotel'
    ),

]
