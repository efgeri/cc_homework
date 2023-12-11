package com.example.codeclan.pirateservice;

import com.example.codeclan.pirateservice.models.Pirate;
import com.example.codeclan.pirateservice.models.Raid;
import com.example.codeclan.pirateservice.models.Ship;
import com.example.codeclan.pirateservice.repository.PirateRepository;
import com.example.codeclan.pirateservice.repository.RaidRepository;
import com.example.codeclan.pirateservice.repository.ShipRepository;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

@RunWith(SpringRunner.class)
@ActiveProfiles("test") //Indicates it's a test profile so will not run DataLoader
@SpringBootTest
public class PirateserviceApplicationTests {

	@Autowired
	PirateRepository pirateRepository;

	@Autowired
	ShipRepository shipRepository;

	@Autowired
	RaidRepository raidRepository;

	@Test
	public void contextLoads() {
	}

	@Test
	public void createPirateAndShipThenSave(){

		Ship dutchman = new Ship("The Flying Dutchman");
		shipRepository.save(dutchman);
		Pirate jack = new Pirate("jack", "sparrow", 32, dutchman);
		pirateRepository.save(jack);
	}

	@Test
	public void createPirateAndRaidThenSave(){
		Ship pineapple = new Ship("The Flying Pineapple");
		shipRepository.save(pineapple);
		Pirate spongeBob = new Pirate("SpongeBob", "SquarePants", 8, pineapple);
		pirateRepository.save(spongeBob);

		Raid raid = new Raid("Tortuga", 100);
		raidRepository.save(raid);

		spongeBob.addRaid(raid);
		raid.addPirate(spongeBob);
		raidRepository.save(raid);
		
	}

	@Test
	public void canFindPiratesOver30 (){
		List<Pirate> found = pirateRepository.findByAgeGreaterThan(30);
		assertEquals(1, found.size());
		assertTrue(found.size() > 0);
	}

	@Test
	public void findRaidByLocation(){
		List<Raid> found = raidRepository.findRaidByLocation("Tortuga");
		assertEquals("Tortuga", found.get(0).getLocation());
	}

	@Test
	public void findPiratesByRaidId(){
	List<Pirate> foundPirates = pirateRepository.findByRaidsId(1L);
	assertEquals(1, foundPirates.size());
	assertEquals("SpongeBob", foundPirates.get(0).getFirstName());
	}

	@Test
	public void canFindShipsWithPirate(){
		List<Ship> found = shipRepository.findShipByPiratesName("jack");
		assertEquals("myes", found);
	}

	@Test
	public void canFindAllRaidsForAGivenShip() {
		Ship foundship = shipRepository.getById(3L);
		List<Raid> foundRaids = raidRepository.findByPiratesShip(foundship);
		assertEquals("Barbados", foundRaids.get(0).getLocation());
	}

}
