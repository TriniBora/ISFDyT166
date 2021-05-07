function cambia_imagen(elemento) {
    var texto = document.getElementById("texto");
    elemento.src = "img/imagen2.jpg";
    texto.innerHTML = "Para familias de hasta 5 personas. Wi-Fi. Pet friendly.";
}

function restaura_imagen(elemento) {
    var texto = document.getElementById("texto");
    elemento.src = "img/imagen.jpg";
    texto.innerHTML = "Alquiler temporario en Tandil, al pie de las Sierras.";
}