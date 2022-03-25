var valorCorreto = randomInt(1,10)
i = 0
function Chutar(){ 
    certo = 0
    var valorDoChute = parseInt(document.getElementById("valor").value)
    if (verificadorDeAcertos(valorDoChute,valorCorreto)){
        document.getElementById("resultado").innerHTML = `Você acerto o valor ${valorCorreto}`
        i = 2
        certo = 1
    }
    else{
        document.getElementById("resultado").innerHTML = `${verificadorDeChutes(valorDoChute,valorCorreto)},
        ja foram ${i+1}°tentativas vc so tem mais ${2-i} tentativas.`;
    }
    i ++
    if (i===3){
        if(certo!==1){
            document.getElementById("resultado").innerHTML ="Você errou 3 vezes,"+
            "O numero correto era "+valorCorreto+" ,o numero vai mudar.";
        }
        setTimeout(function Reiniciar() {
            valorCorreto = randomInt(1,10);
            i = 0
            document.getElementById("resultado").innerHTML = "Poder começar novamente!";
        }, 3000);
    }
}

function verificadorDeAcertos(valorDeUsuario,valorGerado){
    if(valorDeUsuario===valorGerado){
        return true
    }
    else{
        return false
    }
}

function verificadorDeChutes(valorDeUsuario,valorGerado){
    if (valorDeUsuario > valorGerado){
        return "Você chutou muito alto"
    }
    else{
        return "Você chutou muito baixo"
    }
}


function randomInt(valorInicial,valorFinal){
    return Math.floor(Math.random()*valorFinal + valorInicial)    
}
