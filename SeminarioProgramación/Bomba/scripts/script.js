function activar(elemento) {
    var ancho = parseInt(elemento.width);
    var alto = parseInt(elemento.height);

    if (ancho == 512 && alto == 512) {
        cambiar_imagen(elemento);

    } else {
        if (ancho < 512 && alto < 512) {
            elemento.width = ancho * 2;
            elemento.height = alto * 2;
            //console.log(elemento.width);
            //console.log(elemento.height);
        }
    }
}

function desactivar(elemento) {
    var ancho = parseInt(elemento.width);
    var alto = parseInt(elemento.height);

    if (ancho < 512 && alto < 512) {
        elemento.width = ancho / 2;
        elemento.height = alto / 2;
    }
}

function cambiar_imagen(elemento) {
    elemento.src = "imagenes/explosion.png";
    //console.log("Cambio de imagen");
}