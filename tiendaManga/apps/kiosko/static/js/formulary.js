$(function(){
    $("formProductAdd").validate({
        rules:{
            txtSku:{
                required: true,
                minlength: 1
            },
            txtNombre:{
                required: true,
                minlength: 8
            },
            txtPrecio:{
                required: true

            },
            cmbCategoria:{
                required: true
            },
            txtStock:{
                required: true

            },
            txtImg:{
                required: true
            }
        },
        messages:{
            txtSku:{
                required:"Debe ingresar SKU al producto"
            },
            txtNombre:{
                required:"Debe ingresar el nombre"
            },
            txtPrecio:{
                required:"Debe ingresar el precio"
            },
            cmbCategoria:{
                required:"Debe elegir una categoria"
            },
            txtStock:{
                required:"Debe colocar stock del producto"
            },
            txtImg:{
                required:"Debe elegir una imagen para el producto"
            }
        }
    })
})