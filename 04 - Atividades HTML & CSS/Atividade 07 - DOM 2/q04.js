document.addEventListener('DOMContentLoaded', function() {
    var selecionarImagens = document.getElementById("selecionarImagens");
    selecionarImagens.addEventListener("change", selecionarImagem);
});

function selecionarImagem() {
    var nomeImagem = document.getElementById("selecionarImagens").value;
    var novaImg = document.createElement("img");
    novaImg.src = nomeImagem;
    
    var resultado = document.getElementById("resultado");
    resultado.innerHTML = '';
    resultado.appendChild(novaImg);
}
