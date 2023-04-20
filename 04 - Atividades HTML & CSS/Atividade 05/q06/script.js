var altera_cor = document.getElementById("alterar_cor");

altera_cor.addEventListener("click", function() {
    var corpo = document.getElementById("corpo");
    var titulo = document.getElementById("titulo");
    var paragrafo = document.getElementById("paragrafo");

    corpo.style.backgroundColor = "black";
    titulo.style.color = "white";
    paragrafo.style.color = "white";
});

var reverter_cor = document.getElementById("reverter_cor");

reverter_cor.addEventListener("click", function() {
    var corpo = document.getElementById("corpo");
    var titulo = document.getElementById("titulo");
    var paragrafo = document.getElementById("paragrafo");

    corpo.style.backgroundColor = "white";
    titulo.style.color = "black";
    paragrafo.style.color = "black";
});