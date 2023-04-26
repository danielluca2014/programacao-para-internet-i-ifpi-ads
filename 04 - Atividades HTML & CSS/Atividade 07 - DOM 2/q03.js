document.addEventListener('DOMContentLoaded', function() {
    var buttonCarregar = document.getElementById("buttonCarregar");
    buttonCarregar.addEventListener("click", carregarImagem);
});

function carregarImagem() {
    var nomeImagem = document.getElementById("caixaDeTexto").value;
    var novaImg = document.createElement("img");
    var enderecoImagem = `Imagens/${nomeImagem}`;
    novaImg.src = enderecoImagem;
    
    var resultado = document.getElementById("resultado");
    resultado.innerHTML = '';
    resultado.appendChild(novaImg);
}
