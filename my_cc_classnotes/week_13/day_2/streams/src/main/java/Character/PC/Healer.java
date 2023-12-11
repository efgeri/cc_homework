package Character.PC;

import Inventory.Treasure;

import javax.tools.Tool;
import java.util.ArrayList;

public class Healer extends PC{
    private ArrayList<Tool> tools;
    private Tool selectedTools;

    public Healer(int HP, int defence, String name, ArrayList<Tool> tools, Tool selectedTools) {
        super(HP, defence, name);
        this.tools = tools;
        this.selectedTools = selectedTools;
    }

    public Tool getSelectedTools() {
        return selectedTools;
    }

    public void setSelectedTools(Tool selectedTools) {
        this.selectedTools = selectedTools;
    }

    public void heal(){

    }
}
