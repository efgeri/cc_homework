public class FlightManager {
    Flight flight;

    public FlightManager(Flight flight) {
        this.flight = flight;
    }

    public double totalBagWeightAllowance(){
        return flight.getPlane().getWeight() / 2;
    }

    public double totalBagWeight() {
        double totalBags = 0;
        for (Passenger passenger : flight.getPassengerList()){
            totalBags += passenger.getNumberOfBags();
        }
        return totalBags * 10;
    }
    public double totalRemainingWeight() {
        return totalBagWeightAllowance() - totalBagWeight();
    }


}
