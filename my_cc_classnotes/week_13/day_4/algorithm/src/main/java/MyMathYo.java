public class MyMathYo {

    // 0(n²) - exponential time complexity
    public static int squareByCounting(int n){
        int count = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                count++;
            }
        }
        return count;
    }

    public static int squareByAddition(int n){
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum +=n;
        }
        return sum;
    }
//    0(1) - constant time complexity
    public static int squareByLookup(int n){
        int[] lookupTable = {0, 1, 4, 9, 16, 25};
        return lookupTable [n];
    }
}
