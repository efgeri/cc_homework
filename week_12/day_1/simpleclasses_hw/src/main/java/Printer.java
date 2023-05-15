public class Printer {

    private int sheets;
    private int toner;


    public Printer (int sheets){
        this.sheets = sheets;
        this.toner = 100;
    }

    public int getSheets() {
        return this.sheets;
    }

    public int getTonerLevel() {
        return this.toner;
    }
    public void print (int pages, int copies){
        if (pages*copies <= sheets) {
            this.sheets -= pages * copies;
            this.toner -= pages * copies;
        }
    }

}
