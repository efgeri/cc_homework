import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PrinterTest {
    Printer printer;

    @Before
    public void before(){
        printer = new Printer(500);
    }

    @Test
    public void hasPaper(){
        assertEquals(500, printer.getSheets());
    }
    @Test
    public void canPrint(){
        printer.print(10, 3);
        assertEquals(470, printer.getSheets());
    }
    @Test
    public void tooMuchToPrint(){
        printer.print(3900, 3);
        assertEquals(500, printer.getSheets());
    }
    @Test
    public void tooAllowRefusePrint(){
        printer.print(10, 3);
        printer.print(3900, 3);
        assertEquals(470, printer.getSheets());
    }
    @Test
    public void tooRefuseAllowPrint(){
        printer.print(3900, 3);
        printer.print(10, 4);
        assertEquals(460, printer.getSheets());
    }
    @Test
    public void tonerAfterPrinting(){
        printer.print(10, 4);
        assertEquals(60, printer.getTonerLevel());
    }
}
