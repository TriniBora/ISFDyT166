var sumar = function(num1, num2) {
    //return parseInt(num1) + parseInt(num2); //parseInt convierte String a entero
    document.getElementById("rta").innerHTML = num1 + num2;
};

var restar = function(num1, num2) {
    //return parseInt( num1 ) - parseInt( num2 );
    document.getElementById("rta").innerHTML = num1 - num2;
    num1 = num2 = "";
};

var multiplicar = function(num1, num2) {
    //return parseInt( num1 ) * parseInt( num2 );
    document.getElementById("rta").innerHTML = num1 * num2;
};

var dividir = function(num1, num2) {
    //return parseInt( num1 ) / parseInt( num2 );
    document.getElementById("rta").innerHTML = num1 / num2;
};

function ingresar() {
    var num1 = parseInt(document.getElementById("numero1").value);
    var num2 = parseInt(document.getElementById("numero2").value);
    //alert("El primer número fue " + num1 + " y el segundo es " + num2);
    var operacion = document.getElementById("operacion").value;

    if (operacion == "suma") {
        sumar(num1, num2);
    } else if (operacion == "resta") {
        restar(num1, num2);
    } else if (
        operacion == "multiplicacion" ||
        operacion == "multiplicación"
    ) {
        multiplicar(num1, num2);
    } else if (operacion == "division" || operacion == "divisin") {
        dividir(num1, num2);
    } else {
        alert("La operación ingresada no es válida.");
    }
}

function borrar() {
    document.getElementById("numero1").innerHTML = "";
    document.getElementById("numero2").innerHTML = "";
    document.getElementById("operacion").innerHTML = "suma - resta - multiplicación - división";
    document.getElementById("rta").innerHTML = "";
}