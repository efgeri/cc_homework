import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class FlightTest {
    Pilot pilot;
    CabinCrewMember fo;
    CabinCrewMember fa;
    CabinCrewMember cad;
    Passenger passenger;
    Flight flight;
    ArrayList<CabinCrewMember> cabinCrew;


    @Before
    public void before() {
        fo = new CabinCrewMember("Bob", Rank.FIRSTOFFICER);
        fa = new CabinCrewMember("Lisa", Rank.FLIGHTATTENDANT);
        cad = new CabinCrewMember("Roy", Rank.CADET);
        pilot = new Pilot("Maverick", Rank.CAPTAIN, "ABC12345");
        passenger = new Passenger("Tourist Johnny", 3);
        cabinCrew = new ArrayList<>();
        cabinCrew.add(fo);
        cabinCrew.add(fa);
        cabinCrew.add(cad);
        flight = new Flight(pilot, cabinCrew, Plane.AIRBUSA320, "UA119", "EDI", "ORD", "19/05/2023 12:00");
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

}