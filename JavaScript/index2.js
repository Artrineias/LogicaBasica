
let vetor = [1,1,2,3,5,8,13,21,34,55];
let resultado = document.getElementById("resultado")

function addVetor(){
    let entrada = parseInt((document.getElementById("n1")).value)
    add(vetor,entrada)
    mostra(vetor);
}

function add(vet,valor){
    vet.push(valor);
    mostra(vet);
}

function mostra(v){
    resultado.innerHTML = v
}

function mostraPar(){
    let par=[];
    vetor.forEach(variavel => {
        if((variavel%2)==0){
            add(par,variavel)
        }
    });
    mostra(par)
}


function mostraImpar(){
    let impar=[];
    vetor.forEach(variavel => {
        if((variavel%2)!=0){
            add(impar,variavel)
        }
    });
    mostra(impar)
}