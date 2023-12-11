public class Bicycle implements IMove{
    private int distanceTravelled;

    public Bicycle() {
        this.distanceTravelled = 0;
    }

    public int getDistanceTravelled() {
        return distanceTravelled;
    }

    public void move(int distance){
        this.distanceTravelled += distance;
    }


}
