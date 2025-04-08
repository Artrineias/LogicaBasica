function temperaturaK(){
    var temperaturaInicial = parseFloat(document.getElementById("temperatura").value);
    var temperatura = temperaturaInicial + 273.15;
    document.getElementById("temperaturafinal").innerHTML = "K° " + temperatura; 
}
function temperaturaF() {
    var temperaturaInicial = parseFloat(document.getElementById("temperatura").value);
    var temperatura = (temperaturaInicial*(9/5))+32;
    document.getElementById("temperaturafinal").innerHTML = "F° " + temperatura;

}