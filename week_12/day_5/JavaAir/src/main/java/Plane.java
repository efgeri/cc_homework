public enum Plane {

    BOEING737800(189, 41140.00),
    BOEING747(568, 183500.00),
    AIRBUSA320(170, 62500),
    AIRBUSA380(853, 575000);

    private final int capacity;
    private final double weight;

    Plane(int capacity, double weight) {
        this.capacity = capacity;
        this.weight = weight;
    }

    public int getCapacity() {
        return capacity;
    }
}
