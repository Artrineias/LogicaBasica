let prompt = require("prompt-sync")();

let quantidade = prompt("Quantidade de moedas(2,3,4 ou 5): ");
let jogadas = prompt("Quantas jogadas seram feitas: ")
let moeda = null;
let igual = 0, venceu = false, i;
let resultado = []

for ( i = 0; i < jogadas; i++) {
    resultado[i] = []
    for (let j = 0; j < quantidade; j++) {

        moeda = Math.trunc(Math.random() * 2);
        if (moeda == 1) {
            resultado[i][j] = "Cara"
        } else {
            resultado[i][j] = "Coroa"
        }


    }
    if(i>0){
        for (let j = 0; j < quantidade; j++) {
            if (resultado[0][j] == resultado[i][j]) {
                igual++
            }
        }
        if (igual == quantidade) {
            venceu = true;
            break;
        }
    }
}
console.log(resultado)


if (venceu) {
    console.log("Voce venceu, tentativas:", i)
} else {
    console.log("Voce perdeu")
}



