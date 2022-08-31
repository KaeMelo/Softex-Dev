const carro = {
    modelo: 'Azera',
    fabricante: 'Hyundai',
    NomeCompleto: function(){
        return `${this.fabricante} ${this.modelo}`
    }
}
console.log(carro.NomeCompleto());
