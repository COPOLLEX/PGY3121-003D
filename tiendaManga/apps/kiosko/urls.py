from django.urls import path
from .import views 

urlpatterns = [
    path('',views.cargarInicio),

    path('addManga',views.cargarFormulary),
    path('addProduct',views.addProduct),

    path('edditProduct/<id>',views.cargarEdit),
    path('editarFormulario',views.editarProducto),

    path('eliminarProducto/<id>',views.deleteProduct),
    
    path('cargaSeinen',views.cargarSeinen),
    path('cargaShonen',views.cargarShonen),
    path('cargaSpokon',views.cargarSpokon),

    path('insanoRegister',views.loadRegister),
    path('insanoLogin',views.loadLogin),


    #carrito compra
    path('',views.tienda, name ="Tienda")

]