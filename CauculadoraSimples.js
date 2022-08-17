function calcular(oper) {
    var valor1 =  prompt(“Digite o primeiro valor: ”);
    var valor2 =  prompt(“Digite o segundo valor: ”);
 
    if (oper == "somar") {
       var res = parseInt(valor1) + parseInt(valor2);
    } else {
       if (oper == "subtrair") {
          var res = valor1-valor2;
       } else {
          if (oper == "multiplicar") {
             var res = valor1*valor2;
          } else {
             var res = valor1/valor2;
          }
       }
    }

}
