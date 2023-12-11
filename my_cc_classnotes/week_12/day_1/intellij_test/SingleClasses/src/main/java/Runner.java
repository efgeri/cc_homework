public class Runner {
    public static void main(String[] args) {
        Bear instanceOfBear = new Bear("Pooh");
        String name = instanceOfBear.getName();
        System.out.println(name);
        instanceOfBear.setName("Winnie");
        System.out.println(instanceOfBear.getName());
    }
}
