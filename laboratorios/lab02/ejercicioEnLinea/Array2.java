public class Array2{
    public int countEvens(int[] nums) { //exercise 1 //c0
        int count = 0; // c1
        for(int i = 0; i < nums.length; i++){ // n*c2
            if(nums[i]%2 == 0){ // n*c3
                count++; // n*c4
            }
        }
        return count; //c5
    }
    //we get
    //T(n) = c0 + c1 + n*c2 + n*c3 + n*c4 + c5
    //then
    //T(n) = O(n) with n length of nums

    public int bigDiff(int[] nums) { //exercise 2 c0
        int min = nums[0]; // c1
        int max = nums[0]; // c2
        for(int i = 1; i < nums.length; i++){ // (n-1)*c3
            if(nums[i] > max){ //(n-1)*c4
                max = nums[i]; // (n-1)*c5
            }
            else if(nums[i] < min){ // (n-1) * c6
                min = nums[i]; // (n-1) * c7
            }
        }
        return max - min; // c8
    }
    //we get
    //T(n) = c0 + c1 + c2 + (n-1)*c3 + (n-1)*c4 + (n-1)*c5 + c8
    //then
    //T(n) = O(n) with n length of nums

    public int centeredAverage(int[] nums) { //exercise 3 c0
        int min = nums[0]; // c1
        int max = nums[0]; // c2
        int sum = nums[0]; // c3
        for(int i = 1; i < nums.length; i++){ // (n-1) * c4
            if(nums[i] > max){ // (n-1) * c5
                max = nums[i];// (n-1) * c6
            }
            else if(nums[i] < min){// (n-1) * c7
                min = nums[i];// (n-1) * c8
            }
            sum = sum + nums[i];// (n-1) * c9
        }
        return (sum-min-max)/(nums.length-2); //c10
    }
    //we get
    //T(n) = c0 + c1 + c2 +  c3 + (n-1)*c4 + (n-1)*c5 + (n-1)*c6 + (n-1)*c9 + c10
    //then
    //T(n) = O(n) with n length of nums

    public int sum13(int[] nums) { //exercise 4 c0
        int sum = 0;// c1
        for(int i = 0; i < nums.length; i++){//n*c2
            if(nums[i] == 13){//n*c3
                i++;//n*c4
                continue;//n*c5
            }
            sum = sum + nums[i];////n*c6
        }
        return sum;//c7
    }
    //we get
    //T(n) = c0 + c1 + n*c2 + n*c3 + n*c4 + n*c5
    //then
    //T(n) = O(n) with n length of nums

    public int sum67(int[] nums) {//exercise 5 c0
        int sum = 0; //c1
        for(int i = 0; i < nums.length; i++){//n*c2
            if(nums[i] == 6){//n*c3
                while(nums[i] != 7){//n*c4
                    i++;//n*c5
                }
                continue;//n*c6
            }
            sum = sum + nums[i]; //c7
        }
        return sum; //c8
    }
    //we get
    //T(n) = c0 + c1 + n*c2 + n*c3 + n*c4 + n*c5 + n*c6 +c7 +c8
    //then
    //T(n) = O(n) with n length of nums
}