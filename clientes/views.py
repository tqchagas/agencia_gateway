from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import View

from gateway import clientes


class ClienteNovo(View):
    def get(self, request):
        return render(request, 'cadastrar.html')

    def post(self, request):
        clientes.salvar_cliente(request.POST)
        return HttpResponseRedirect('/clientes/')


class ClienteAtualizar(View):
    def get(self, request, pk):
        return render(
            request,
            'atualizar.html',
            {"cliente": clientes.buscar_cliente(pk)})

    def post(self, request, pk=None):
        clientes.atualizar_cliente(pk, request.POST)
        return HttpResponseRedirect('/clientes/')


class ClienteDetalhe(View):
    def get(self, request, pk):
        return render(
            request,
            'detalhe.html',
            {"cliente": clientes.buscar_cliente(pk)})


class ClienteListar(View):
    def get(self, request):
        return render(
            request,
            'listar.html',
            {"clientes": clientes.buscar_cliente()})


class ClienteApagar(View):
    def get(self, request, pk):
        return render(
            request,
            'apagar.html',
            {"cliente": clientes.buscar_cliente(pk)})

    def post(self, request, pk):
        clientes.apagar_cliente(pk)
        return HttpResponseRedirect('/clientes/')
