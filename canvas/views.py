from django.shortcuts import render
from django.shortcuts import redirect
from canvas.models import SuitModelCanvas
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator



def index(request):
    if request.method == 'POST':
        return new_smc(request)
    else:
        return render(request, 'index.html')

def new_smc(request):
    smc = SuitModelCanvas()
    smc.save()
    return redirect(f'/smc/{smc.pk}')

def conf_del_smc(request, pk):
    return render(request, 'conf_del_smc.html', {'pk': pk})

def del_smc(request, pk):
    smc = get_object_or_404(SuitModelCanvas, pk=pk)
    smc.delete()
    smc = SuitModelCanvas.objects.all().last()
    return redirect(f'/smc/{smc.pk}')


def smc(request, pk):
    smc = get_object_or_404(SuitModelCanvas, pk=pk)
    qs = SuitModelCanvas.objects.all()

    # unpack the queryset into a list, then use the inbuilt Python index function to determine smc instance position.
    actual_page = (*qs,).index(smc)
    
    #finds the previous and prox (next) smc if exists
    prev = actual_page
    prox = actual_page

    try:
        prev = (qs[actual_page - 1]).pk
    except ValueError:
        prev = (qs[actual_page]).pk
        print("Não existe SMC anterior ao atual")
        
    try:
        prox = (qs[actual_page + 1]).pk
    except IndexError:
        prox = (qs[actual_page]).pk
        print("Não existe SMC posterior ao atual")


    if request.method == "POST":
        smc.pretensao = request.POST.get('pretensao-text') or smc.pretensao
        smc.requisitos_documentais = request.POST.get('requisitos-documentais-text') or smc.requisitos_documentais
        smc.nome_peca = request.POST.get('nome-peca-text') or smc.nome_peca
        smc.causa_pedir = request.POST.get('causa-pedir-text') or smc.causa_pedir
        smc.pedidos = request.POST.get('pedidos-text') or smc.pedidos
        smc.beneficios = request.POST.get('beneficios-text') or smc.beneficios
        smc.partes_processo = request.POST.get('partes-processo-text') or smc.partes_processo
        smc.terceiros = request.POST.get('terceiros-text') or smc.terceiros
        smc.competencia = request.POST.get('competencia-text') or smc.competencia
        smc.equipe = request.POST.get('equipe-text') or smc.equipe
        smc.provas = request.POST.get('provas-text') or smc.provas
        smc.entregas_processuais = request.POST.get('entregas-processuais-text') or smc.entregas_processuais
        smc.restricoes = request.POST.get('restricoes-text') or smc.restricoes
        smc.riscos = request.POST.get('riscos-text') or smc.riscos
        smc.prazos = request.POST.get('prazos-text') or smc.prazos
        smc.honorarios = request.POST.get('honorarios-text') or smc.honorarios
        smc.demais_despesas = request.POST.get('demais-despesas-text') or smc.demais_despesas
        smc.ementa = request.POST.get('ementa-text') or smc.ementa
            
        smc.save()
        
        if request.htmx:
            # return 204 No Content - HTTP
            return HttpResponse(status=204)
    else:
        return render(request, 'smc.html', {'smc': smc,
                                            'prev': prev,
                                            'prox': prox,
                                            'len_qs': len(qs)})
