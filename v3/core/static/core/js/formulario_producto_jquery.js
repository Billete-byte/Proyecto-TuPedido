
jQuery.extend(jQuery.validator.messages, {
    required: "Este campo es obligatorio.",
    remote: "Por favor, rellena este campo.",
    email: "Por favor, escribe una dirección de correo válida",
    url: "Por favor, escribe una URL válida.",
    date: "Por favor, escribe una fecha válida.",
    dateISO: "Por favor, escribe una fecha (ISO) válida.",
    number: "Por favor, escribe un número entero válido.",
    digits: "Por favor, escribe sólo dígitos.",
    creditcard: "Por favor, escribe un número de tarjeta válido.",
    equalTo: "Por favor, escribe el mismo valor de nuevo.",
    accept: "Por favor, escribe un valor con una extensión aceptada.",
    maxlength: jQuery.validator.format("Por favor, no escribas más de {0} caracteres."),
    minlength: jQuery.validator.format("Por favor, no escribas menos de {0} caracteres."),
    rangelength: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1} caracteres."),
    range: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1}."),
    max: jQuery.validator.format("Por favor, escribe un valor menor o igual a {0}."),
    min: jQuery.validator.format("Por favor, escribe un valor mayor o igual a {0}.")
});

var validator = $("#formularioProducto").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 80
            //email:true,
            //date:true
        },
        tipo_producto: {
            required: true
        },
        precio: {
            required: true,
            number: true,
            min: 1,
            max: 500
        },
        informacion:{
            required:true,
            minlength:10,
            maxlength:200
        }

    },
    messages: {
        nombre: {
            minlength: "Debe tener 3 caracteres!!!!!!!!"
        }
    }
});

function cargarProductos() {
    var url = "https://cine.mycm.cl/api/pelicula";


    $.get(url, function (result) {
        var html = `
                <tr>
                    <th>Nombre</th>
                    <th>Precio</th>
                    <th>Stock</th>
                    <th>¿Descuento?</th>
                    <th>Tipo_producto</th>
                    <th>informacion</th>
                </tr>
            `;

        result.forEach(function (item) {

            html += `
                    <tr>
                        <td>${item.nombre}</td>
                        <td>${item.precio}</td>
                        <td>${item.stock}</td>
                        <td>${(item.descuento) ? 'si' : 'no'}</td>
                        <td>${item.tipo_producto}</td>
                        <td>${item.informacion.substring(0, 20)}</td>
                    </tr>
                `;
        });


        //document.getElementById("tablaPeliculas").innerHTML = html;
        $("#tablaProductos").html(html);
    });



}



function cargarTipos_productos() {
    var url = "https://cine.mycm.cl/api/genero";

    fetch(url)
        .then(function (result) {
            return result.json();
        })
        .then(function (result) {

            var html = `<option value=''>Seleccionar</option>`;

            result.forEach(function (item) {
                html += `<option value='${item.id}'>${item.nombre}</option>`;
            });

            document.getElementById("tipo_producto").innerHTML = html;

        });
}

$("#btnEnviar").click(function () {

    if (validator.form()) {
        var nombre = $("#nombre").val();
        console.log(nombre);
        var precio = $("#precio").val();
        var tipo_producto = $("#tipo_producto").val();
        var informacion = $("#informacion").val();

        var esDescuento = $("#esDescuento").is(":checked");

        var stock = $("input[name='stock']:checked").val();

        var data = {
            "nombre": nombre,
            "precio": precio,
            "informacion": informacion,
            "es_descuento": esdescuento,
            "stock": stock,
            "tipo_procuto_id": tipo_producto
        };

        var url = "https://cine.mycm.cl/api/pelicula";

        $.ajax({
            'url': url,
            'data': JSON.stringify(data),
            'type': 'post',
            'headers': {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            'success': function (result) {
                
                /*Swal.fire({
                    title:'Felicitaciones',
                    text:'La pelicula fue guardada correctamente',
                    //type:'success',
                    imageUrl:'img/gatito.jpg',
                    timer:2000
                });*/

                toastr.success("Producto guardado correctamente", "Felicitaciones",{
                    'positionClass':'toast-bottom-right'
                });

                //error
                //warning
                //info

                cargarProductos();
            },
            'error': function () {
                console.log("ha fallado!!! :c");
            }
        });

    }



});


cargarTipos_productos();
cargarProductos();