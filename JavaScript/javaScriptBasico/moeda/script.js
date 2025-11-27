function Converter() {
    var valorMoedaInicial = parseFloat(document.getElementById("valor").value);
    var valorMoedaFinal = 5;
    var valorMostrado = valorMoedaInicial / valorMoedaFinal;
    document.getElementById("valorConvertido").innerHTML =
      "Valor em Dolar é U$" + valorMostrado;
  }
  