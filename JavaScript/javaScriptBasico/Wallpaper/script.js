var listaFilme = [] 

function atualizar(){
    var imagem = document.getElementById("imagem").value;
    listaFilme.push(imagem)
    adicionarFilmes()
}

function adicionarFilmes(){
    for(var i=0 ; i< listaFilme.length ; i++){
        document.getElementById("img").innerHTML += `<img class 
        ="imgem," src="${listaFilme[i]}">`; 
    } 
}

