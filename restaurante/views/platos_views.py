
from django.shortcuts import redirect, render
from restaurante.forms import PlatosForm
from restaurante.models import Platos

def platos_list(request):
    platos = Platos.objects.all()
    return render(
        request,
        "restaurante/platos/list.html",
        {
            "platos": platos
        }
    )

def platos_create(request):
    form = PlatosForm()

    if request.method == "POST":
        form = PlatosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("platos_list")
    return render(
        request,
        "restaurante/platos/form.html",
        {
            "form": form
        }
    )

def platos_edit(request, id):
    plato = Platos.objects.get(id=id)
    form = PlatosForm(instance=plato)

    if request.method == "POST":
        form = PlatosForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect("platos_list")
    return render(
        request,
        "restaurante/platos/form.html",
        {
            "form": form
        }
    )

def platos_delete(request, id):
    plato = Platos.objects.get(id=id)
    plato.delete()
    return redirect("platos_list")
