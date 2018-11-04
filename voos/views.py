from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import View

from gateway import voos


class VooNovo(View):
    def get(self, request):
        aeroportos = voos.buscar_aeroporto()
        return render(
            request,
            'voos/cadastrar.html',
            {"aeroportos": aeroportos}
        )

    def post(self, request):
        voos.salvar_voo(request.POST)
        return HttpResponseRedirect('/voos/')


class VooAtualizar(View):
    def get(self, request, pk):
        return render(
            request,
            'voos/atualizar.html',
            {
                "aeroportos": voos.buscar_aeroporto(),
                "voo": voos.buscar_voo(pk)
            }
        )

    def post(self, request, pk=None):
        voos.atualizar_voo(pk, request.POST)
        return HttpResponseRedirect('/voos/')


class VooDetalhe(View):
    def get(self, request, pk):
        return render(
            request,
            'voos/detalhe.html',
            {"voo": voos.buscar_voo(pk)})


class VooListar(View):
    def get(self, request):
        return render(
            request,
            'voos/listar.html',
            {"voos": voos.buscar_voo()})


class VooApagar(View):
    def get(self, request, pk):
        return render(
            request,
            'voos/apagar.html',
            {"voo": voos.buscar_voo(pk)})

    def post(self, request, pk):
        voos.apagar_voo(pk)
        return HttpResponseRedirect('/voos/')
