public class App {
    public static void main(String[] args) throws Exception {
        Ninja shikamaru = new Ninja("Shikamaru", 17, "Folha", "Kagemane no Jutsu",Kekkei_Genkai.Uchiha("uchiha","Folha"));
        System.out.println(shikamaru.getJutsu_Principal());
        System.out.println(shikamaru.getIdade());
    }
}
