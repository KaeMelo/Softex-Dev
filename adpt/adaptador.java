package adpt;

import adpt.compo.AdaptadorPato;
import adpt.comp.Galinha;
import adpt.com.Pato;
import adpt.comp.PatoReal;

public class AdptadorPatoDemo {
    public static void main(String[] args) {
        Pato patoReal = new PatoReal();
        Galinha galinha = new AdaptadorPato(patoReal);

        System.out.println(patoReal.fazerQuaQua());
        System.out.println(patoReal.voar());

        System.out.println(galinha.fazerCocorico());
        System.out.println(galinha.voar());
    }
    
}
