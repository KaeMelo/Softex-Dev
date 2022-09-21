var cliente = {
    banco: "Itaú",
    titular: "Kae",
    conta: "Poupança",
    agencia: 111, 
    saldo: 350 ,
    numConta: 40028922,

}

var saque = function(valor){
    cliente.saldo = cliente.saldo - valor;
}

var deposito = function(valor){
    cliente.saldo = cliente.saldo + valor;
}

var retornarSaldo = function(){
    console.log("Saldo: " + cliente.saldo);
}

var retornarCliente = function(){
    console.log("Banco:" + cliente.banco);
    console.log("Titular:" + cliente.titular);
    console.log("Conta:" + cliente.conta);
    console.log("Agência:" + cliente.agencia);
    console.log("Saldo:" + cliente.saldo);
    console.log("Número da conta:" + cliente.numConta);
}

retornarCliente();

deposito(100.00);
retornarSaldo();
saque(20);
retornarSaldo();
