function Somar(){
    var notaDoPrimeiroBimestre = parseFloat((document.getElementById("nota_1")).value)
    var notaDoSegundoBimestre = parseFloat((document.getElementById("nota_2")).value)
    var notaDoTerceiroBimestre = parseFloat((document.getElementById("nota_3")).value)
    
    var notaFinal = (notaDoPrimeiroBimestre+ notaDoSegundoBimestre + notaDoTerceiroBimestre)/3
    var notaFixa = notaFinal.toFixed(1)
    document.getElementById("soma").innerHTML = "Nota final é " +notaFixa; 
  }