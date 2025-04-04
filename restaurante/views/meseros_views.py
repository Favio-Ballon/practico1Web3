from django.shortcuts import redirect, render
from restaurante.forms import MeserosForm
from restaurante.models import Meseros

def meseros_list(request):
    meseros = Meseros.objects.all()
    return render(
        request,
        "restaurante/meseros/list.html",
        {"meseros": meseros}
    )

def meseros_create(request):
    if request.method == "POST":
        form = MeserosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("meseros_list")
    else:
        form = MeserosForm()
    return render(
        request,
        "restaurante/meseros/form.html",
        {"form": form}
    )

def meseros_edit(request, id):
    mesero = Meseros.objects.get(id=id)
    if request.method == "POST":
        form = MeserosForm(request.POST, instance=mesero)
        if form.is_valid():
            form.save()
            return redirect("meseros_list")
    else:
        form = MeserosForm(instance=mesero)
    return render(
        request,
        "restaurante/meseros/form.html",
        {"form": form}
    )

def meseros_delete(request, id):
    mesero = Meseros.objects.get(id=id)
    mesero.delete()
    return redirect("meseros_list")
