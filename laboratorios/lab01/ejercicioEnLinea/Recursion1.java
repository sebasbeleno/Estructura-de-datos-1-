
public class Recursion1 {

    /**
     * Compute recursively the total number of blocks in such a triangle with the
     * given number of rows.
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.0
     * @param rows - The number of row of the triangle
     * @return int - the total number of blocks in such a triangle with the given
     *         number of rows
     */
    public int triangle(int rows) { // excercise 1 c0
        if (rows == 0) { // c1
            return 0; // c2
        }
        return triangle(rows - 1) + rows; // T1(n-1) + c3

        // we get
        // T1(n) = c1 + c2 + c0 if n = 0
        // T1(n) = T1(n-1) + c4 = c4n + c5
        // then
        // T1(n) = O(n) with n = rows
    }

    /**
     * Compute recursively the total number of ears for a fiven bunnies where the
     * odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..)
     * we'll say have 3 ears
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.1
     * @param bunnies - The number of bunnies
     * @return int - The total number of ears for a given bunnies number
     */
    public int bunnyEars2(int bunnies) { // excercise 2 c0
        if (bunnies == 0) { // c1
            return 0; // c2
        } else if (bunnies % 2 != 0) { // c3
            return bunnyEars2(bunnies - 1) + 2; // c4 + T(n-1)
        } else {
            return bunnyEars2(bunnies - 1) + 3; // c4 + T(n-1)

            // we get
            // T(n) = c1 + c2 + c0 if n = 0
            // T(n) = T(n-1) + T(n-1) + c5 = c5*((2**n) -1) + c6*2**n-1
            // then
            // T(n) = O(2**n) with n = bunnies
        }
    }

    /**
     * Given a non-negative int n, return the sum of its digits recursively
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.0
     * @param n - A non-negative number
     * @return int - The sum of its digits
     */
    public int sumDigits(int n) { // excercise 3 c0
        if (n < 10) { // c1
            return n; // c2
        }
        return sumDigits(n / 10) + n % 10; // T(m-1) + c3

        // we get
        // T(m) = c1 + c2 + c0 if m <= 1
        // T(m) = T(m-1) + c4 = c4m + c5
        // then
        // T(m) = O(m) with m being the number of digits of n
    }

    /**
     * Given a non-negative int n, return the count of the occurrences of 7 as a
     * digit
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.0
     * @param n - A non-negative number
     * @return int - The count of the occurrences of 7 as a digit
     */
    public int count7(int n) { // excercise 4 c0
        if (n < 10) { // c1
            if (n == 7) { // c2
                return 1; // c3
            }
            return 0; // c3
        }
        return count7(n / 10) + count7(n % 10); // T(m-1) + T(1)

        // we get
        // T(m) = c1 + c2 + c3 + c0 if m = 1
        // T(m) = T(m-1) + T(1) + c5
        // However T(1) = c3 + c2 + c1
        // then
        // T(m) = T(m-1) + c7 = c7m + c8
        // then
        // T(m) = O(m) with m being the number of digits of n
    }

    /**
     * Compute recursively the nth fibonacci number
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.0
     * @param n - A fibonacci number
     * @return int - The n'th fibonacci number
     */
    public int fibonacci(int n) { // excercise 5 c0

        if (n <= 1) { // c1
            return n; // c2
        }

        return fibonacci(n - 1) + fibonacci(n - 2); // c3 + T(n-1) + T(n-2)
        // we get
        // T(m) = c0 + c1 + c2, if n <=1
        // T(m) = c3 + T(m-1) + T(m-2) = T(n) = c3*2**m + c4
        // then
        // T(m) = O(2**m) with m being the number of digits of n
    }
}
