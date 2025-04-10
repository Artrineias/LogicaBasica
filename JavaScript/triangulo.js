let prompt = require("prompt-sync")();


function main(){
    console.log("Digite o valor dos lados do triangulos: ");
    const ladoA = Number(prompt("Lado A: "));
    const ladoB = Number(prompt("Lado B: "));
    const ladoC = Number(prompt("Lado C: "));

    if(verificarsetriangulo(ladoA,ladoB,ladoC)){
        console.log("Você tem um triangulo.");
        verificarqualtriangulo(ladoA,ladoB,ladoC);

    }

}

function verificarsetriangulo(ladoA,ladoB,ladoC){
    if((ladoA + ladoB) > ladoC && (ladoA + ladoC) > ladoB && (ladoB + ladoC) > ladoA){
        return true;
    }
    return false;
}

function verificarqualtriangulo(a,b,c){
    if(equilatero(a,b,c)){
        console.log("Equilatero, a = ",a,",b = ",b,",c = ",c," todos os lados são iguais.");
    }else if(isoscele(a,b,c)){
        console.log("Isosceles, a = ",a,",b = ",b,",c = ",c," dois lados são iguais.");
    }else if(escaleno(a,b,c)){
        console.log("Escaleno, a = ",a,",b = ",b,",c = ",c," todos os lados diferentes.");
    }
}

function equilatero(a,b,c){
    if((a==b)&&(b==c)){
        return true;
    }
    return false;
}
function isoscele(a,b,c){
    if(a==b&&c!=a||c==a&&c!=b){
        return true;
    }
    return false;
}
function escaleno(a,b,c){
    if((a!=b)&&(b!=c)&&(a!=c)){
        return true;
    }
    return false;
}

main()