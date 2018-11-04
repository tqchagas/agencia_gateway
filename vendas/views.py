from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import View

from gateway import vendas


class VendaView(View):
    def get(self, request):
        return render(request, 'vendas/cadastrar.html')

    def post(self, request):
        vendas.salvar_cliente(request.POST)
        return HttpResponseRedirect('/vendas/')


class VendaDetalhe(View):
    def get(self, request, pk):
        return render(
            request,
            'vendas/detalhe.html',
            {"venda": vendas.buscar_venda(pk)})


class VendaListar(View):
    def get(self, request):
        return render(
            request,
            'vendas/listar.html',
            {"vendas": vendas.buscar_venda()})


class VendaApagar(View):
    def get(self, request, pk):
        return render(
            request,
            'vendas/apagar.html',
            {"venda": vendas.buscar_venda(pk)})

    def post(self, request, pk):
        vendas.apagar_venda(pk)
        return HttpResponseRedirect('/vendas/')
