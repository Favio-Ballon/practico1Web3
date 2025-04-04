from django.shortcuts import redirect, render
from restaurante.forms import MesaForm
from restaurante.models import Mesa

def mesas_list(request):
    mesas = Mesa.objects.all()
    return render(
        request,
        "restaurante/mesas/list.html",
        {"mesas": mesas}
    )

def mesas_create(request):
    if request.method == "POST":
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mesas_list")
    else:
        form = MesaForm()
    return render(
        request,
        "restaurante/mesas/form.html",
        {"form": form}
    )

def mesas_edit(request, id):
    mesa = Mesa.objects.get(id=id)
    if request.method == "POST":
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect("mesas_list")
    else:
        form = MesaForm(instance=mesa)
    return render(
        request,
        "restaurante/mesas/form.html",
        {"form": form}
    )

def mesas_delete(request, id):
    mesa = Mesa.objects.get(id=id)
    mesa.delete()
    return redirect("mesas_list")