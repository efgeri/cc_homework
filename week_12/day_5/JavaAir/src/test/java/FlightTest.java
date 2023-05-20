import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;

import static org.junit.Assert.assertEquals;

public class FlightTest {
    Pilot pilot;
    CabinCrewMember fo;
    CabinCrewMember fa;
    CabinCrewMember cad;
    Passenger passenger;
    Flight flight;
    ArrayList<CabinCrewMember> cabinCrew;
    Calendar departure;



    @Before
    public void before() {
        fo = new CabinCrewMember("Bob", Rank.FIRSTOFFICER);
        fa = new CabinCrewMember("Lisa", Rank.FLIGHTATTENDANT);
        cad = new CabinCrewMember("Roy", Rank.CADET);
        pilot = new Pilot("Maverick", "ABC12345");
        passenger = new Passenger("Tourist Johnny", 3);
        cabinCrew = new ArrayList<>();
        cabinCrew.add(fo);
        cabinCrew.add(fa);
        cabinCrew.add(cad);
        departure = Calendar.getInstance();
        departure.set(2023, Calendar.MAY, 19, 14, 33);
        flight = new Flight(pilot, cabinCrew, Plane.AIRBUSA320, "UA119", "EDI", "ORD", departure);

    }


   @Test
    public void bookPassenger() {
        flight.bookPassenger(passenger);
        assertEquals(1, flight.getPassengerList().size());
    }
    @Test
    public void canGetAvailSeats() {
        flight.bookPassenger(passenger);
        assertEquals( 169, flight.getAvailSeats());
    }
    @Test
    public void pilotCanFly() {
        assertEquals( "Punch it!", pilot.fly());
    }
    @Test
    public void crewCanRelay() {
        assertEquals( "The captain's message is the following!", fo.relayMessage());
    }
    @Test
    public void hasDepartureTime() {
        String departureString = flight.getDepartureTime().get(Calendar.YEAR) + "-"
                + (flight.getDepartureTime().get(Calendar.MONTH) + 1) + "-"
                + flight.getDepartureTime().get(Calendar.DAY_OF_MONTH) + " "
                + flight.getDepartureTime().get(Calendar.HOUR_OF_DAY) + ":"
                + flight.getDepartureTime().get(Calendar.MINUTE);
        assertEquals( "2023-5-19 14:33", departureString);
    }

}