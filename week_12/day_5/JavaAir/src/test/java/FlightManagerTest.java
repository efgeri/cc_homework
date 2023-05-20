import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Calendar;

import static org.junit.Assert.assertEquals;

public class FlightManagerTest {
    Pilot pilot;
    CabinCrewMember fo;
    CabinCrewMember fa;
    CabinCrewMember cad;
    Passenger passenger;
    Flight flight;
    ArrayList<CabinCrewMember> cabinCrew;
    FlightManager flightManager;
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
        flightManager = new FlightManager(flight);
    }

    @Test
    public void canGetTotalBagAllowance(){
        assertEquals(31250.00, flightManager.totalBagWeightAllowance(), 0.00);
    }

    @Test
    public void canGetReservedBagWeight(){
        flight.bookPassenger(passenger);
        assertEquals(30, flightManager.totalBagWeight(), 0.00);
    }
    @Test
    public void canGetRemainingWeight(){
        flight.bookPassenger(passenger);
        assertEquals(31220.00, flightManager.totalRemainingWeight(), 0.00);
    }
}
