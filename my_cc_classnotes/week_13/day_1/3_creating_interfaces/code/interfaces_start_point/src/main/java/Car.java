public class Car implements IMove, IFuel{
    private String make;
    private String model;
    private int odometerReading;

    private int fuelReading;

    public Car(String make, String model){
        this.make = make;
        this.model = model;
        this.odometerReading = 0;
        this.fuelReading = 0;
    }

    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public int getOdometerReading() {
        return odometerReading;
    }

    @Override
    public void move(int distance) {
        this.odometerReading += distance;
        this.fuelReading -= distance;
    }

    @Override
    public int getFuelReading() {
        return this.fuelReading;
    }

    @Override
    public void addFuel(int litres) {
        this.fuelReading += litres;
    }
}
