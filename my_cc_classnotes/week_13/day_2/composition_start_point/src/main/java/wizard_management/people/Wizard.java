package wizard_management.people;


import behaviours.IFlyable;
import wizard_management.cleaning.Broomstick;

public class Wizard {
    String name;
    IFlyable ride;

    public Wizard(String name, IFlyable ride){
        this.name = name;
        this.ride = ride;
    }

    public String getName(){
        return this.name;
    }

    public IFlyable getRide(){
        return this.ride;
    }

    public String fly(){
        return this.ride.fly();
    }

    public void setRide(IFlyable ride) {
        this.ride = ride;
    }
}
