package prototype;

public class moto extends Veiculo {

    private int comprimento;
    private int cargaMin;

    /**
     * @param modelo
     * @param marca
     * @param cor
     * @param nuemroRodas
     * @param comprimento
     * @param cargaMin
     */
    public moto(String modelo, String marca, String cor, int nuemroRodas, int comprimento, int cargaMin) {
        super(modelo, marca, cor);
        super.setNumeroRodas(nuemroRodas);
        this.comprimento = comprimento;
        this.cargaMin = cargaMin;
    }

    @Override
    public Veiculo clone() {
        return new moto(getModelo(), getMarca(), getCor(), getNumeroRodas(), comprimento, cargaMin);
    }

    @Override
    public String reprensent() {
        return super.reprensent() + String.format("Comprimento: %dm\nCarga minima: %d peso", comprimento, cargaMin);
    }
