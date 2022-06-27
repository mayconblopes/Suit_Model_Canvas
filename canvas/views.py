from django.shortcuts import render
from django.shortcuts import redirect
from canvas.models import SuitModelCanvas
from django.shortcuts import get_object_or_404



def index(request):
    if request.method == 'POST':
        return new_smc(request)
    else:
        return render(request, 'index.html')

def new_smc(request):
    smc = SuitModelCanvas()
    smc.save()
    return redirect(f'smc/{smc.pk}')


def smc(request, pk):
    smc = get_object_or_404(SuitModelCanvas, pk=pk)
    if request.method == "POST":
        smc.pretensao = request.POST.get('pretensao-text')
        smc.save()
        return redirect(f'/smc/{smc.pk}')
    else:
        return render(request, 'smc.html', {'smc': smc})