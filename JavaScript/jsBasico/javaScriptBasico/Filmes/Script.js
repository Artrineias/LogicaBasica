function Main(){
    var campoFilmes = document.getElementById("filme").value
    if (verifadorImagem(campoFilmes)){
        adicionarFilme(campoFilmes)
    }
    document.getElementById("filme").value = ""
}

function verifadorImagem(campoFilmes){
    if(campoFilmes.endsWith(".jpg")||campoFilmes.endsWith(".png")){
        return true
    }
    else{
        return false
    }
}

function adicionarFilme(campoFilmes){
    var elementoFilmeFavorito = `<img src="${campoFilmes}">`
    var listaFilmes = document.getElementById("listaFilmes")
    listaFilmes.innerHTML += elementoFilmeFavorito
}
