from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Vino, Cliente, Venta
from .forms import VinoForm, ClienteForm, VentaForm


def home(request):
    vinos = Vino.objects.filter(activo=True).order_by("-id")[:3]
    return render(request, "gestion/home.html", {"vinos": vinos})

def vinos_disponibles(request):
    vinos = Vino.objects.filter(activo=True).order_by("-id")
    return render(request, "gestion/vinos_disponibles.html", {"vinos": vinos})



@login_required
def vino_listar(request):
    vinos = Vino.objects.all().order_by("-id")
    return render(request, "gestion/vino_listar.html", {"vinos": vinos})


@permission_required("gestion.add_vino", login_url="login", raise_exception=True)
def vino_crear(request):
    if request.method == "POST":
        form = VinoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("vino_listar")
    else:
        form = VinoForm()

    return render(request, "gestion/vino_form.html", {"form": form})


@permission_required("gestion.change_vino", login_url="login", raise_exception=True)
def vino_editar(request, id):
    vino = get_object_or_404(Vino, id=id)

    if request.method == "POST":
        form = VinoForm(request.POST, request.FILES, instance=vino)

        if form.is_valid():
            form.save()
            return redirect("vino_listar")
    else:
        form = VinoForm(instance=vino)

    return render(request, "gestion/vino_form.html", {"form": form})


@permission_required("gestion.delete_vino", login_url="login", raise_exception=True)
def vino_eliminar(request, id):
    vino = get_object_or_404(Vino, id=id)

    if request.method == "POST":
        vino.delete()
        return redirect("vino_listar")

    return render(request, "gestion/vino_confirmar_eliminar.html", {"vino": vino})


@permission_required("gestion.change_vino", login_url="login", raise_exception=True)
def vino_toggle(request, id):
    vino = get_object_or_404(Vino, id=id)

    vino.activo = not vino.activo
    vino.save()

    return redirect("vino_listar")




@login_required
def cliente_listar(request):
    clientes = Cliente.objects.all().order_by("-id")
    return render(request, "gestion/cliente_listar.html", {"clientes": clientes})


@permission_required("gestion.add_cliente", login_url="login", raise_exception=True)
def cliente_crear(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("cliente_listar")
    else:
        form = ClienteForm()

    return render(request, "gestion/cliente_form.html", {"form": form})


@permission_required("gestion.change_cliente", login_url="login", raise_exception=True)
def cliente_editar(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect("cliente_listar")
    else:
        form = ClienteForm(instance=cliente)

    return render(request, "gestion/cliente_form.html", {"form": form})


@permission_required("gestion.delete_cliente", login_url="login", raise_exception=True)
def cliente_eliminar(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.delete()
        return redirect("cliente_listar")

    return render(request, "gestion/cliente_confirmar_eliminar.html", {"cliente": cliente})



@login_required
def venta_listar(request):
    ventas = Venta.objects.all().order_by("-fecha")
    return render(request, "gestion/venta_listar.html", {"ventas": ventas})


@permission_required("gestion.add_venta", login_url="login", raise_exception=True)
def venta_crear(request):
    if request.method == "POST":
        form = VentaForm(request.POST)

        if form.is_valid():
            venta = form.save(commit=False)
            venta.usuario = request.user
            venta.save()
            return redirect("venta_listar")
    else:
        form = VentaForm()

    return render(request, "gestion/venta_form.html", {"form": form})