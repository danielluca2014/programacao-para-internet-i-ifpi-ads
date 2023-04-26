document.addEventListener('DOMContentLoaded', function() {
    let botaoValidar = document.getElementById("botaoValidar");
    botaoValidar.addEventListener("click", validarCheckbox);
});

function validarCheckbox() {
    let checkbox = document.getElementsByName("opcao");
    marcado = false;

    let i = 0;
    while (i < checkbox.length) {
        if (checkbox[i].checked) {
            marcado = true;
            break;
        }
        i++;
    }
    
    if (marcado) {
        alert("Pelo menos um checkbox marcado.");

    } else {
        alert("Nenhum checkbox marcado.");
    }
}