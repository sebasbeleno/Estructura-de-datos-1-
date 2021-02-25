
public class Bat1{

    /**
     * Compute recursively the total number of blocks in such a triangle with the given number of rows.
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.0
     * @param rows - The number of row of the triangle
     * @return int - the total number of blocks in such a triangle with the given number of rows
     */
    public int triangle(int rows) { //excercise 1
        if(rows == 0){ 
            return 0;
        }
        return triangle(rows -1) + rows;
    }

    /**
     * Compute recursively the total number of ears for a fiven bunnies where 
     * the odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..)
     * we'll say have 3 ears
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.1
     * @param bunnies - The number of bunnies 
     * @return int - The total number of ears for a given bunnies number
     */
    public int bunnyEars2(int bunnies) { //excercise 2
        if (bunnies == 0) { 
            return 0;
        }
        if(bunnies%2 != 0){
            return bunnyEars2(bunnies -1) + 2;
        }
       
        return bunnyEars2(bunnies -1) + 3;
        
    }

    /**
     * Given a non-negative int n, return the sum of its digits recursively
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.0
     * @param n - A non-negative number 
     * @return int - The sum of its digits
     */
    public int sumDigits(int n) { //excercise 3
        if(n < 10){
            return n;
        }
        return sumDigits(n/10) + n%10;
    }

    /**
     * Given a non-negative int n, return the count of the occurrences of 7 as a digit
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.0
     * @param n - A non-negative number 
     * @return int - The count of the occurrences of 7 as a digit
     */
    public int count7(int n) { //excercise 4
        if(n < 10){
            if(n == 7){
                return 1;
            }
            return 0;
        }
        return count7(n/10) + count7(n%10);
    }
 
    /**
     * Compute recursively the nth fibonacci number
     * 
     * @authors Jairo Marulanda - Sebastian Beleño
     * @version v1.0
     * @param n - A fibonacci number
     * @return int - The n'th fibonacci number
     */
    public int fibonacci(int n) { //excercise 5

        if (n <= 1){
            return n;
        }

        return fibonacci(n -1) + fibonacci(n - 2);
    }

}