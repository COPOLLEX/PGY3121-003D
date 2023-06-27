const formulario = document.getElementById("formProductAdd")

formulario.addEventListener('submit',function(evento){
    evento.preventDefault();

    //sku
    if (document.getElementById("txtSku").value.length == 0) {
        alert("Debe ingresar el codigo del producto.");
    }else{
        this.submit();
    }
    //nombre
    if (document.getElementById("txtNombre").value.length == 0){
        alert("Porfavor ingrese un nombre para el manga")
    }else{
        this.submit();
    }
    //Precio
    if (document.getElementById("txtPrecio").value.length == 0){
        alert("Porfavor ingrese el precio del manga")
    }else{
        this.submit();
    }
    //categoria ta malo
    if (document.getElementById("cmbCategoria").value.length == 0){
        alert("Porfavor Seleccione una categoria")
    }else{
        this.submit();
    }
    //Stock
    if (document.getElementById("txtStock").value.length == 0){
        alert("El stock no debe ser 0")
    }else{
        this.submit();
    }
    //StocktxtDescripcion
    if (document.getElementById("txtDescripcion").value.length == 0){
        alert("Añade una descripcion al manga")
    }else{
        this.submit();
    }

})