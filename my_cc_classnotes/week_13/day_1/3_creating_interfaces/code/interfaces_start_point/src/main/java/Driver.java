public class Driver {
    public void drive(IMove vehicle, int distance){
        vehicle.move(distance);
    }

    public void usePetrol(IFuel iFuel, int litres){
        iFuel.addFuel(litres);
    }
}
