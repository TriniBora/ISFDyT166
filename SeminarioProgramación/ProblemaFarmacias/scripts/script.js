var cajas1 = 100;
var jarabe1 = 100;
var expectorante1 = 150;

var cajas2 = 90;
var jarabe2 = 140;
var expectorante2 = 100;
var colectivo2 = 5;

function farmaciaUno() {
    var subTotal = ((cajas1 * 2) + jarabe1 + expectorante1);
    var retencionIva = subTotal * 1.1;
    return subTotal + retencionIva;
}

function farmaciaDos() {
    var subTotal = ((cajas2 * 2) + jarabe2 + expectorante2 + colectivo2);
    var retencionIva = subTotal * 1.15;
    return subTotal + retencionIva;
}

function precioFarmaciaUno() {
    precio = farmaciaUno();
    console.log('El costo en la Farmacia 1 es: $' + precio);
}

function precioFarmaciaDos() {
    precio = farmaciaDos();
    console.log('El costo en la Farmacia 2 es: $' + precio);
    //$('#farmacia').show();
}



function consultar() {
    var precio1 = farmaciaUno();
    var precio2 = farmaciaDos();

    var ahorro = precio1 - precio2;

    if (ahorro < 0) {
        console.log('En la farmacia 1 se ahorra $ ' + Math.abs(ahorro));
    } else {
        if (ahorro > 0) {
            console.log('En la farmacia 2 se ahorra $ ' + Math.abs(ahorro));
        } else {
            console.log('En las dos farmacias le sale lo mismo $ ' + precio1);
        }
    }
}