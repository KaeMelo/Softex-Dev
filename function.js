function quadrado(numero) {
    quad = numero * numero;
    return quad;
}
var num = prompt("Digite um número: ");
document.write("O quadrado de" + num + "é" + quadrado(num));
