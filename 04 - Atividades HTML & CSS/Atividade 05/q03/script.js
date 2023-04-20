var botao = document.getElementById("botao");

botao.addEventListener("click", function() {
    var paragrafo = document.getElementById("paragrafo");
    paragrafo.textContent = "O texto deste parágrafo foi alterado!";
});

var limpar = document.getElementById("limpar");

limpar.addEventListener("click", function() {
    var paragrafo = document.getElementById("paragrafo");
    paragrafo.textContent = "";
});
