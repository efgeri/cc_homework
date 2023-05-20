import java.util.ArrayList;
import java.util.Calendar;

public class Flight {
    private Pilot pilot;
    private ArrayList<CabinCrewMember> crewMemberList;
    private ArrayList<Passenger> passengerList;
    private Plane plane;
    private String flightNumber;
    private String origin;
    private String destination;
    private Calendar departureTime;

    public Flight(Pilot pilot, ArrayList<CabinCrewMember> crewMemberList, Plane plane, String flightNumber, String origin, String destination, Calendar departureTime) {
        this.pilot = pilot;
        this.crewMemberList = crewMemberList;
        this.passengerList = new ArrayList<>();
        this.plane = plane;
        this.flightNumber = flightNumber;
        this.origin = origin;
        this.destination = destination;
        this.departureTime = departureTime;
    }

    public int getAvailSeats (){
        return (this.plane.getCapacity() - passengerList.size());
    }

    public void bookPassenger(Passenger passenger){
        if (this.getAvailSeats() > 0) {passengerList.add(passenger);};
    }

    public ArrayList<Passenger> getPassengerList() {
        return passengerList;
    }

    public Plane getPlane() {
        return plane;
    }

    public Calendar getDepartureTime() {
        return departureTime;
    }
}
