function Calculadora() {
    let n1 = parseFloat(document.getElementById("n1").value);
    let operacao = document.getElementById("operacao").value;
    let n2 = parseFloat(document.getElementById("n2").value);
    let resultado = document.getElementById("resultado")
    switch (operacao) {
        case "+":
            resultado.innerHTML = soma(n1, n2)
            break
        case "-":
            resultado.innerHTML = subtracao(n1, n2)
            break
        case "*":
            resultado.innerHTML = multiplicacao(n1, n2)
            break
        case "/":
            resultado.innerHTML = divisao(n1, n2)
            break
    }


}
function soma(a, b) {
    return a + b;
}

function subtracao(a, b) {
    return a - b;
}

function divisao(a, b) {
    return a / b;
}

function multiplicacao(a, b) {
    return a * b;
}