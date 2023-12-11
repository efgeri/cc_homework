public class Runner {
    public static void main(String[] args) {
        Planet mars = new Planet("Mars", 937659);
        System.out.printf("%s is %d big! %n", mars.getName(), mars.getSize());
        mars.explode();
    }
}
