from django.shortcuts import redirect, render
from restaurante.forms import OrdenesForm, AddPlato, OrdenesEditForm
from restaurante.models import Ordenes, OrdenPlato, Platos, Meseros


def ordenes_list(request):
    ordenes = Ordenes.objects.all()

    return render(
        request,
        "restaurante/ordenes/list.html",
        {"ordenes": ordenes}
    )

def ordenes_create(request):
    if request.method == "POST":
        form = OrdenesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ordenes_list")
    else:
        form = OrdenesForm()
    return render(
        request,
        "restaurante/ordenes/form.html",
        {"form": form}
    )

def ordenes_edit(request, id):
    orden = Ordenes.objects.get(id=id)
    if request.method == "POST":
        form = OrdenesEditForm(request.POST, instance=orden)
        if form.is_valid():
            meseroId = form.cleaned_data["mesero"].id
            mesero = Meseros.objects.get(id=meseroId)
            orden.mesero = mesero
            orden.save()
            return redirect("ordenes_list")
    else:
        form = OrdenesEditForm(instance=orden)
    return render(
        request,
        "restaurante/ordenes/form.html",
        {"form": form}
    )

def ordenes_delete(request, id):
    orden = Ordenes.objects.get(id=id)
    orden.delete()
    return redirect("ordenes_list")

def agregar_plato(request, id):
    orden = Ordenes.objects.get(id=id)
    if request.method == "POST":
        form = AddPlato(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            plato_id = request.POST.get("plato")
            plato = Platos.objects.get(id=plato_id)
            cantidad = form.cleaned_data["cantidad"]
            orden_plato, created = OrdenPlato.objects.get_or_create(
                orden=orden,
                plato=plato,
                defaults={"cantidad": cantidad}
            )
            if not created:
                orden_plato.cantidad += cantidad
                orden_plato.save()
            return redirect("ordenes_list")
    form = AddPlato()
    platos = OrdenPlato.objects.filter(orden=orden)
    return render(
        request,
        "restaurante/ordenes/agregar_plato.html",
        {"orden": orden, "platos": platos, "form": form}
    )

def eliminar_plato(request,id):
    orden_plato = OrdenPlato.objects.get(id=id)
    orden_plato.delete()
    return redirect("ordenes_list")
