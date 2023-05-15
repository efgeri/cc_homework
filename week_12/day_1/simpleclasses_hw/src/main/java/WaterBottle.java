public class WaterBottle {

    private int volume;

    public WaterBottle (){
        this.volume = 100;
    }

    public void drink(){
        if (this.volume > 10) {this.volume -= 10;}
        else {this.empty();}
    }

    public int getVolume() {
        return this.volume;
    }
    public void empty() {
        this.volume = 0;
    }
    public void fill() {
        this.volume = 100;
    }
}
