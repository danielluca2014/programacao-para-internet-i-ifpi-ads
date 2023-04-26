document.addEventListener('DOMContentLoaded', function () {
    var botaoSomar = document.getElementById('botaoSomar');
    botaoSomar.addEventListener('click', exibirResultado);
});

function exibirResultado() {
    var valor1 = Number(document.getElementById('caixaDeTexto1').value);
    var valor2 = Number(document.getElementById('caixaDeTexto2').value);

    if (isNaN(valor1) || isNaN(valor2)) {
        alert("Os valores devem ser números!");
    }
    
    var resultado = valor1 + valor2;
    
    alert(`A soma é ${resultado}.`);
}
