public class Pilot extends CabinCrewMember{
    private String licenceNumber;


    public Pilot(String name, String licenceNumber) {
        super(name, Rank.CAPTAIN);
        this.licenceNumber = licenceNumber;
    }

    public String getLicenceNumber() {
        return licenceNumber;
    }

    public void setLicenceNumber(String licenceNumber) {
        this.licenceNumber = licenceNumber;
    }

    public String fly(){
        return "Punch it!";
    }
}
