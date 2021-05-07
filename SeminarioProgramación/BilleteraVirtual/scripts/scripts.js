//Sumar Variable;
var amount_ = 17450;
document.getElementById('amount_').innerHTML = amount_;

function refresh(amount_) {
    document.getElementById('amount_').innerHTML = amount_;
    $('#ingreso').val('');
    $('#egreso').val('');
    $('#ingresos').hide();
    $('#egresos').hide();

}

function add() {
    $('#ingresos').show();
}

function agregarDinero() {
    var acreditar = $('#ingreso').val();
    amount_ = amount_ + parseInt(acreditar);
    refresh(amount_);
    var historial = document.getElementById('history').innerHTML;
    document.getElementById('history').innerHTML = '<p class="txn-list">Ingreso dinero<span class="credit-amount">+$' + acreditar + '</span></p>' + historial;
}

function remove() {
    $('#egresos').show();
}

function debitarDinero() {
    var debitar = $('#egreso').val();
    amount_ = amount_ - parseInt(debitar);
    refresh(amount_);
    var historial = document.getElementById('history').innerHTML;
    document.getElementById('history').innerHTML = '<p class="txn-list">Pago servicio<span class="debit-amount">+$' + debitar + '</span></p>' + historial;
}