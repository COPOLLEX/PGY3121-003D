from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import os
from django.http import HttpResponse
import json
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.
def cargarInicio(request):
    return render(request,'inicio.html')

def cargarSeinen(request):
    seinen = Product.objects.filter(categoryID = 1)
    return render(request,'seinen.html',{"mangaSeinen":seinen})

def cargarShonen(request):
    shonen = Product.objects.filter(categoryID = 2)
    return render(request,'shonen.html',{"mangaShonen":shonen})

def cargarSpokon(request):
    spokon = Product.objects.filter(categoryID = 3)
    return render(request,'spokon.html',{"mangaSpokon":spokon})


def cargarFormulary(request):
    categorias = Category.objects.all
    products = Product.objects.all
    return render(request,'mangas.html',{"cate":categorias,"prod":products})


def cargarEdit(request,id):
    categorias = Category.objects.all
    products = Product.objects.get(idProduct = id)

    categoriasID = products.categoryID

    prodCateID = Category.objects.get(idCategory = categoriasID.idCategory).idCategory

    return render(request,"editarManga.html",{"prod":products,"cate":categorias,"categoriasID":prodCateID})


def addProduct(request):
    print(request.POST)
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_precio = request.POST['txtPrecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_img = request.FILES['txtImg']
    

    categoria = Category.objects.get(idCategory = request.POST['cmbCategoria'])
    
    Product.objects.create(
        idProduct = v_sku , 
        name = v_nombre , 
        valor = v_precio, 
        stock = v_stock,
        description = v_descripcion,
        img_url = v_img, 
        categoryID = categoria)
    
    return redirect('/addManga')


def editarProducto(request):
    v_sku = request.POST['txtSku']
    productoBD = Product.objects.get(idProduct = v_sku)
    v_nombre = request.POST['txtNombre']
    v_precio = request.POST['txtPrecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']

    categoria = Category.objects.get(idCategory = request.POST['cmbCategoria'])

    try:
        v_img = request.FILES['txtImg']
        ruta_imagen  = os.path.join(settings.MEDIA_ROOT, str(productoBD.img_url))
        os.remove(ruta_imagen)
    except:
        v_img = productoBD.img_url

    productoBD.name = v_nombre
    productoBD.valor = v_precio
    productoBD.stock = v_stock
    productoBD.description = v_descripcion
    productoBD.categoryID = categoria
    productoBD.img_url = v_img  

    productoBD.save()

    return redirect('/addManga')

def deleteProduct(request,id):
    producto = Product.objects.get(idProduct = id)
    producto.delete()
    ruta_imagen  = os.path.join(settings.MEDIA_ROOT, str(producto.img_url))
    os.remove(ruta_imagen)

    return redirect('/addManga')


#register
def loadRegister(request):

    if request.method == 'GET':
            return render(request,"register.html", {
            'form': UserCreationForm
    })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('/insanoLogin')

            except IntegrityError:
                return render(request,"register.html", {
                'form': UserCreationForm,
                'error': 'El usuario ya existe'
                })

        return render(request,"register.html", {
            'form': UserCreationForm, 
            'error' : 'Las contraseñas no son iguales'
            })

#login
def loadLogin(request):
    if request.method == 'GET':
        return render(request,"login.html", {
        'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request,"login.html", {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrecta'
             })
        else:
            login(request,user)
            return redirect('/')


def tienda(request):
    return render(request, "tienda.html")