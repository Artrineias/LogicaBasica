public class Ninja {
    private  String nome;
    private  int idade;
    private  String aldeia;
    private  String jutsu_Principal;
    private  Kekkei_Genkai cla;

    public Ninja(String nome, int idade, String aldeia, String jutsu_Principal, Kekkei_Genkai cla) {
        this.nome = nome;
        this.idade = idade;
        this.aldeia = aldeia;
        this.jutsu_Principal = jutsu_Principal;
        this.cla = cla;

    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }
    
    public String getAldeia() {
        return aldeia;
    }
    public void setAldeia(String aldeia) {
        this.aldeia = aldeia;
    }
    
    public String getJutsu_Principal() {
        return jutsu_Principal;
    }
    public void setJutsu_Principal(String jutsu_Principal) {
        this.jutsu_Principal = jutsu_Principal;
    }
    
}
