package Character;

public abstract class Characters {
    String name;

    private int HP;
    private int defence;

    public Characters(int HP, int defence, String name) {
        this.name = name;
        this.HP = HP;
        this.defence = defence;
    }

    public int getHP() {
        return HP;
    }

    public void setHP(int HP) {
        this.HP = HP;
    }

    public int getDefence() {
        return defence;
    }

    public void setDefence(int defence) {
        this.defence = defence;
    }
}
