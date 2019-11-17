

$(document).ready(function() {

    $("formulario").validate({
        rules:{
            txtCelular:{
                required:true,
                minlength:3,
                maxlength:20
                //email:true,
                //date:true
            },
            cboComuna: {
                required:true
            },
            txtFechaN: {
                required:true,
                number:true,
                min:1950,
                max:2018
            },
            txtNombre:{
                required:true,
                minlength:3,
                maxlength:20
            }

        },
        messages: {
            txtCelular:{
                required:"Campo requerido",
                minlength:"Este campo debe tener al menos 3 caracteres",
                maxlength:"Este campo debe tener como maximo 20 caracteres"
            },
            cboComuna: {
                required:"Eliga una opción"
            },
            txtFechaN:{ 
                required:"Este campo es requerido",
                min:"El año minima es 1950",
                max:"No puede ingresar un año superior a 2018"
            },
            txtNombre: {
                required:"Este campo es requerido",
                minlength:"Minimo 3 caracteres",
                maxlength:"Maximo 20 caracteres"
            }
        }
    });

});