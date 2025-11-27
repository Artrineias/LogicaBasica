public abstract class Kekkei_Genkai {
    private String nome_Cla;
    private String aldeia;
    private String afinidade;

    public Kekkei_Genkai(String nome_Cla, String aldeia) {
        this.nome_Cla = nome_Cla;
        this.aldeia = aldeia;
    }

    public String getNome_Cla() {
        return nome_Cla;
    }
    public void setNome_Cla(String nome_Cla) {
        this.nome_Cla = nome_Cla;
    }

    public String getAldeia() {
        return aldeia;
    }
    public void setAldeia(String aldeia) {
        this.aldeia = aldeia;
    }

    public String getAfinidade() {
        return afinidade;
    }

    public void setAfinidade(String afinidade) {
        this.afinidade = afinidade;
    }
}
