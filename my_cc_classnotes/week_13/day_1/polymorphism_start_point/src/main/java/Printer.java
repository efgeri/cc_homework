public class Printer implements IConnectable{

    public String print(String data){
        return "printing: " + data;
    }

    @Override
    public String getStatus() {
        return "Ink low";
    }
}