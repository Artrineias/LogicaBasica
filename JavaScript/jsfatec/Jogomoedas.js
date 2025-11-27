let prompt = require("prompt-sync")();
 
let quantidade = prompt("Quantidade de moedas(2,3,4 ou 5): ");
let jogadas = prompt("Quantas jogadas seram feitas: ")
let moeda = null;
 
let resultado  = []
 
for(let i = 0; i<jogadas;i++){
    resultado[i] = []
    for(let j = 0; j<quantidade; j++){
 
        moeda =Math.trunc(Math.random()*2);
        if(moeda == 1){
            resultado[i][j] = "Cara"
        }else{
            resultado[i][j] = "Coroa"
        }
 
 
    }
}
console.log(resultado)