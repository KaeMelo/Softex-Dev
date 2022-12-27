package Rest;

import Rest.comp.Sanduiche;
import Rest.comp.ingredientes.Pepperoni;
import Rest.comp.ingredientes.QueijoMussRalado;
import Rest.comp.sanduiches.FrangoAssado;

public class Restaurante {
    public static void main(String[] args) {
        Sanduiche sanduiche = new FrangoAssado();
        sanduiche = new Pepperoni(sanduiche);
        sanduiche = new QueijoMussRalado(sanduiche);

        System.out.println("O " + sanduiche.getDescricao());
        System.out.printf("custa R$%.2f", sanduiche.custo());
    }
    
}
