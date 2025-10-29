import java.lang.System;

public class Main {
    /**
     * Calculates the nth term of the Fibonacci sequence.
     * Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
     * Each number is the sum of the two preceding ones.
     *
     * @param n The term to calculate in the Fibonacci sequence (starting from 0)
     * @return The nth term of the Fibonacci sequence
     */
    public static int fibonacci(int n) {
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }

        int a = 0;
        int b = 1;
        int c;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    /**
     * The main function.
     *
     * @param args The command line arguments.
     */
    public static void main(String[] args) {
        final int n = Integer.parseInt(args[0]);
        System.out.printf("fibonacci(%d) = %d\n", n, fibonacci(n));
    }
}
