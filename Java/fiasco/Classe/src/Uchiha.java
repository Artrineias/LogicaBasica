

public class Uchiha  extends  Kekkei_Genkai{

    boolean sharingamAtivo;
    boolean mangekyouAtivo;
    boolean temVisao;
    boolean amaterasuAtivo;
    boolean tsukuyomiAtivo;
    boolean susanooAtivo;
    
    


    public Uchiha(String nome_Cla, String aldeia, boolean sharingamAtivo, boolean mangekyouAtivo, boolean temVisao,
            boolean amaterasuAtivo, boolean tsukuyomiAtivo, boolean susanooAtivo) {
        super(nome_Cla, aldeia);
        this.sharingamAtivo = false;
        this.mangekyouAtivo = false;
        this.temVisao = true;
        this.amaterasuAtivo = false;
        this.tsukuyomiAtivo = false;
        this.susanooAtivo = false;
    }

    public void  ativarMangekyou(){
        if(sharingamAtivo){
            setmangekyouAtivo(true);
            System.out.println("Ele ativou o Mangekyou Sharingam...");
        }else{
            System.out.println("O Sharingam nao esta ativo...");
        }
    }
    public boolean ismangekyouAtivo() {
        return mangekyouAtivo;
    }
    private  void setmangekyouAtivo(boolean mangekyouAtivo) {
        this.mangekyouAtivo = mangekyouAtivo;
    }


    public boolean isTemVisao() {
        return temVisao;
    }

    public void setTemVisao(boolean temVisao) {
        this.temVisao = temVisao;
    }

    public boolean isAmaterasuAtivo() {
        return amaterasuAtivo;
    }
    public void  ativarAmaterasu(){
        if(mangekyouAtivo){
            setAmaterasuAtivo(true);
            System.out.println("Ele ativou o Amaterasu... Agora seu alvo esta queimando ate sua morte");
        }else{
            System.out.println("O Amaterasu nao esta ativo...");
        }
    }
    private void setAmaterasuAtivo(boolean amaterasuAtivo) {
        this.amaterasuAtivo = amaterasuAtivo;
    }

    public boolean isTsukuyomiAtivo() {
        return tsukuyomiAtivo;
    }
    public void  ativarTsukuyomi(){
        if(mangekyouAtivo){
            setTsukuyomiAtivo(true);
            System.out.println("Ele ativou o Tsukuyomi... Agora seu alvo esta no reino dos pesadelos");
        }else{
            System.out.println("O Sharingam nao esta ativo...");
        }
    }
    private void setTsukuyomiAtivo(boolean tsukuyomiAtivo) {
        this.tsukuyomiAtivo = tsukuyomiAtivo;
    }

    public boolean isSusanooAtivo() {
        return susanooAtivo;
    }
    public void  ativarSusanoo(){
        if(mangekyouAtivo){
            setSusanooAtivo(true);
            System.out.println("Ele ativou o Susanoo... Agora seu corpo tem uma Armadura de chakara gigante");
        }else{
            System.out.println("O Sharingam nao esta ativo...");
        }
    }
    private void setSusanooAtivo(boolean susanooAtivo) {
        this.susanooAtivo = susanooAtivo;
    }

    public boolean isSharingamAtivo() {
        return sharingamAtivo;
    }
    public  void setSharingamAtivo(boolean sharingamAtivo) {
        this.sharingamAtivo = sharingamAtivo;
    }



}
