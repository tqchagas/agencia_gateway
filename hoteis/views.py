from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import View

from gateway import hoteis


class HotelNovo(View):
    def get(self, request):
        return render(request, 'hoteis/cadastrar.html')

    def post(self, request):
        hoteis.salvar_hotel(request.POST)
        return HttpResponseRedirect('/hoteis/')


class HotelAtualizar(View):
    def get(self, request, pk):
        return render(
            request,
            'hoteis/atualizar.html',
            {"hotel": hoteis.buscar_hotel(pk)})

    def post(self, request, pk=None):
        hoteis.atualizar_hotel(pk, request.POST)
        return HttpResponseRedirect('/hoteis/')


class HotelDetalhe(View):
    def get(self, request, pk):
        return render(
            request,
            'hoteis/detalhe.html',
            {"hotel": hoteis.buscar_hotel(pk)})


class HotelListar(View):
    def get(self, request):
        return render(
            request,
            'hoteis/listar.html',
            {"hoteis": hoteis.buscar_hotel()})


class HotelApagar(View):
    def get(self, request, pk):
        return render(
            request,
            'hoteis/apagar.html',
            {"hotel": hoteis.buscar_hotel(pk)})

    def post(self, request, pk):
        hoteis.apagar_hotel(pk)
        return HttpResponseRedirect('/hoteis/')
