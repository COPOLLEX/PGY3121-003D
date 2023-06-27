from django.db import models

# Create your models here.

class Category(models.Model):
    idCategory = models.IntegerField(primary_key=True)
    nameCategory = models.CharField(max_length=50,null=True)

    def __str__(self):
        txt = "nombre: {0} - ID : {1}"
        return txt.format(self.nameCategory,self.idCategory)


class Product(models.Model):
    idProduct = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,null=False)
    valor = models.IntegerField(null=False)
    categoryID = models.ForeignKey(Category,on_delete=models.CASCADE)
    stock = models.IntegerField(null=False)
    description = models.CharField(max_length=150 ,null=False)
    img_url = models.ImageField(upload_to='imagenesProducto')
    
    fecADD = models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "Codigo: {0} - Nombre: {1} - Categoria: {2} -  fecha: {3}"
        return txt.format(self.idProduct, self.name,self.categoryID ,self.fecADD)
    

