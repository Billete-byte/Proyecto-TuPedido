



function cargarTipos_productos() {
    var url = "https://cine.mycm.cl/api/genero";

    fetch(url)
        .then(function(result){
            return result.json();
        })
        .then(function(result) {
            
            var html = `<option value=''>Seleccionar</option>`;

            result.forEach(function(item) {
                html+=`<option value='${item.id}'>${item.nombre}</option>`;
            });

            document.getElementById("tipos_productos").innerHTML = html;

        });
}


function cargarProductos() {
    var url = "https://cine.mycm.cl/api/pelicula";

    fetch(url)
        .then(function (result) {
            return result.json();
        })
        .then(function (result) {

            var html = `
                <tr>
                    <th>Nombre</th>
                    <th>Precio</th>
                    <th>Stock</th>
                    <th>¿Descuento?</th>
                    <th>Tipo_producto</th>
                    <th>Informacions</th>
                </tr>
            `;

            result.forEach(function (item) {

                html += `
                    <tr>
                        <td>${item.nombre}</td>
                        <td>${item.precio}</td>
                        <td>${item.stock}</td>
                        <td>${(item.descuento) ? 'si' : 'no'}</td>
                        <td>${item.tipo_producto.nombre}</td>
                        <td>${item.informacion.substring(0, 20)}</td>
                    </tr>
                `;
            });


            document.getElementById("tablaProductos").innerHTML = html;

        });

}

var btnEnviar = document.getElementById("btnEnviar");

//agregamos un escuchador en el boton cuando hagan click
btnEnviar.addEventListener("click", function () {

    var nombre = document.getElementById("nombre").value;
    console.log(nombre);
    var tipo_producto = document.getElementById("tipo_producto").value;
    console.log(tipo_producto);
    var precio = document.getElementById("precio").value;
    console.log(precio);

    var descuento = document.getElementById("descuento").checked;
    console.log(descuento);

    var informacion = document.getElementById("informacion").value;
    console.log(informacion);


    var stock = "";

    document.getElementsByName("stock")
        .forEach(function (item) {
            if (item.checked) {
                stock = item.value;
            }
        });

    console.log(stock);


    //document.getElementById("nombre").value = "nombre asignado desde js";

    var data = {
        "nombre": nombre,
        "precio": precio,
        "informacion": informacion,
        "es_descuento": esdescuento,
        "stock": stock,
        "tipo_procuto_id": tipo_producto
    };

    var url = "https://cine.mycm.cl/api/pelicula";

    fetch(url, {
        method:"post",
        headers: {
            "Accept":"application/json",
            "Content-Type":"application/json"
        },
        body:JSON.stringify(data)
    })
    .then(function(result) {
        return result.json();
    })
    .then(function(result){
        console.log(result);
        cargarProductos();
    });


});

//realizamos una llamada asincrona a la api de mindicador.cl

var url = "https://mindicador.cl/api";

fetch(url) // se hace la llamada
    .then(function (result) { //se espera a que la llamada termine y 
        //se convierte en json
        return result.json();
    })
    .then(function (result) {//se obtiene el json
        console.log(result);
        var uf = Math.round(result.uf.valor);
        document.getElementById("ufHoy").innerHTML = uf;
        var dolar = Math.round(result.dolar.valor);
        document.getElementById("dolarHoy").innerHTML = dolar;
        var utm = Math.round(result.utm.valor);
        document.getElementById("utmHoy").innerHTML = utm;
        var euro = Math.round(result.euro.valor);
        document.getElementById("euroHoy").innerHTML = euro;

    });


cargarProductos();
cargarTipos_productos();
