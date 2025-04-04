from django.shortcuts import render, redirect
from restaurante.forms import ClienteForm
from restaurante.models import Cliente, Ordenes


def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(
        request,
        "restaurante/clientes/list.html",
        {"clientes": clientes}
    )

def clientes_create(request, id):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            ordenes = Ordenes.objects.get(id=id)
            # Save cliente to ordenes and update estado to false
            ordenes.cliente = cliente
            ordenes.estado = False
            ordenes.save()
            return redirect("ordenes_list")
    else:
        form = ClienteForm()
    return render(
        request,
        "restaurante/clientes/form.html",
        {"form": form}
    )

def clientes_edit(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes_list")
    else:
        form = ClienteForm(instance=cliente)
    return render(
        request,
        "restaurante/clientes/form.html",
        {"form": form}
    )

def clientes_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()