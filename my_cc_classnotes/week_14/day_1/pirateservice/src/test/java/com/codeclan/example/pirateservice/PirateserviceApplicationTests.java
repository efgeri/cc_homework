package com.codeclan.example.pirateservice;

import com.codeclan.example.pirateservice.models.Pirate;
import com.codeclan.example.pirateservice.repositories.PirateRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class PirateserviceApplicationTests {
	@Autowired
	PirateRepository pirateRepository;

	@Test
	void contextLoads() {
	}

	@Test // NEW
	public void createPirate(){
		Pirate jack = new Pirate("Jack", "Sparrow", 32);
		pirateRepository.save(jack);
	}

}
