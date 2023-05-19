public class CabinCrewMember extends Person{
    Rank rank;
    public CabinCrewMember(String name, Rank rank) {
        super(name);
        this.rank = rank;
    }

    public Rank getRank() {
        return rank;
    }

    public void setRank(Rank rank) {
        this.rank = rank;
    }

    public String relayMessage(){
        return "The captain's message is the following!";
    }
}
