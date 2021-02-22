public class Bat1{
    public int triangle(int rows) { //excercise 1
        if(rows == 0){
            return 0;
        }
        return triangle(rows -1) + rows;
    }

    public int bunnyEars2(int bunnies) { //excercise 2
        if (bunnies == 0) {
            return 0;
        }
        else if(bunnies%2 != 0){
            return bunnyEars2(bunnies -1) + 2;
        }
        else{
            return bunnyEars2(bunnies -1) + 3;
        }
    }

    public int sumDigits(int n) { //excercise 3
        if(n < 10){
            return n;
        }
        return sumDigits(n/10) + n%10;
    }

    public int count7(int n) { //excercise 4
        if(n < 10){
            if(n == 7){
                return 1;
            }
            return 0;
        }
        return count7(n/10) + count7(n%10);
    }

    public int fibonacci(int n) { //excercise 5
        if(n == 0) {
            return 0;
        }
        else if(n == 1){
            return 1;
        }
        return fibonacci(n -1) + fibonacci(n - 2);
    }

}