function confirmarEliminacion(id){

    Swal.fire({
        title: 'Estas seguro?',
        text: "no podras deshacer esta opcion!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'si, Eliminar!',
        cancelButtonText: 'cancelar'
      }).then((result) => {
        if (result.value) {
         // redirigir ala ruta eliminar

         window.location.href = "/eliminar-producto/"+id+"/";

        }
      })
}