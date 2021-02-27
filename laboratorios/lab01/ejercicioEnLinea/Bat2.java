
public class Bat2
{

    public boolean groupSum6(int start, int[] nums, int target) { //excersie 1 //c0
        boolean add; //c1
        boolean add_not = false; //c2
        if(start >= nums.length){ //c3
            return target == 0; //c4
        }
        if(nums[start] == 6){ //c5
            add = groupSum6(start +1, nums, target - nums[start]); //T(n-1) + c6
        }
        else{
            add = groupSum6(start +1, nums, target - nums[start]); // T(n-1) + c7
            add_not = groupSum6(start +1, nums, target); //T(n-1) + c8
        }
        return add || add_not; //c9
    }
    //we get
    // T(n) = c0 + c1 + c2 + c3 + c4 if n == 0
    //worst case:
    // T(n) = T(n-1) + T(n-1) + C = C*((2**n)-1) + c11*2**n-1
    //then
    //T(n) = O(2**n) with n being the lenght of nums 

    public boolean groupNoAdj(int start, int[] nums, int target)  { //excersie 2 c0
        boolean add; //c1
        boolean add_not = false; //c2
        if(start >= nums.length){ // c3
            return target == 0; // c4
        }
        add = groupNoAdj(start +2, nums, target - nums[start]); // T(n-2) + c5
        add_not = groupNoAdj(start +1, nums, target); // T(n-1) + c6
        return add || add_not; //c7
    }
    //we get
    // T(n) = c0 + c1 + c2 + c3 + c4 if n == 0
    //worst case:
    // T(n) = T(n-2) + T(n-1) + C = Fibbonachi = c8*2**n + c9
    //then
    //T(n) = O(2**n) with n being the lenght of nums 

    public boolean groupSum5(int start, int[] nums, int target) { //excersie 3 //c0
        boolean add = false; //c1
        boolean add_not = false; //c2

        if(start >= nums.length){ //c3
            return target == 0; //c4
        }

        if(nums[start]%5 == 0){ //c5
            add = groupSum5(start +1, nums, target - nums[start]); //T(n-1)
        }
        else if(start != 0 && nums[start -1] == 5 && nums[start] == 1){ // c6
            add_not = groupSum5(start +1, nums, target); // T(n-1)
        }
        else{
            add = groupSum5(start +1, nums, target - nums[start]); //T(n-1)
            add_not = groupSum5(start +1, nums, target); //T(n-1)
        }
        return add || add_not; //c7
    }
    //we get
    // T(n) = c0 + c1 + c2 + c3 + c4 if n == 0
    //worst case:
    // T(n) = T(n-1) + T(n-1) + C = C*((2**n)-1) + c9*2**n-1
    //then
    //T(n) = O(2**n) with n being the lenght of nums 

    public boolean groupSumClump(int start, int[] nums, int target) { //excersie 4 c0
        boolean add = false; //c1
        boolean add_not = false; //c2
        if(start >= nums.length){ //c3
            return target == 0; //c4
        }

        if(start-1 != -1 && nums[start-1] == nums[start] ){ // c5
            add= groupSumClump(start +1, nums, target - nums[start]); // T(-1)
            add_not = groupSumClump(start +1, nums, target + nums[start]); //T(-1)
        }
        else if(start+1 != nums.length && nums[start+1] == nums[start] ){ //c8
            add= groupSumClump(start +1, nums, target - nums[start]); //T(-1)
            add_not = groupSumClump(start +1, nums, target + nums[start]); //T(-1)
        }
        else{
            add =groupSumClump(start +1, nums, target - nums[start]); //T(-1)
            add_not = groupSumClump(start +1, nums, target); //T(-1)
        }
        return  add || add_not; //c9
    }
    //we get
    // T(n) = c0 + c1 + c2 + c3 + c4 if n == 0
    //worst case:
    // T(n) = T(n-1) + T(n-1) + C = C*((2**n)-1) + c11*2**n-1
    //then
    //T(n) = O(2**n) with n being the lenght of nums 

    public boolean splitArray(int[] nums) { //excercise 5 //c0
        int n = sumArray(nums,nums.length); //P(n) + c1
        if(n%2 != 0){ //c2
            return false; //c3
        }
        return groupSum(0, nums, n/2); //G(n) + c4
    }
    //we get
    //T(n) = P(n) + c1 + c0 + c10 + c11 + c12 if n == 0
    //worst case:
    // T(n) = P(n) + c1 + G(n) + c4 + C = c8*n + c9 + c1 + C*((2**n)-1) + c18*2**n-1 + c18 + c4 + C
    //then
    //T(n) = O(2**n) with n being the lenght of nums 

    public int sumArray(int[] nums, int pos){ // Aux excercise 5 c5
        if(pos <= 0){ //c5
            return 0; //c7
        }
        return sumArray(nums, pos - 1) + nums[pos - 1]; //P(n-1) + c8
    }
    //we get
    // P(n) = c4 + c5 + c6 if n == 0
    //worst case:
    // P(n) = P(n-1) + c8 = c8*n + c9
    //then
    //P(n) = O(n) with n being the lenght of nums 
    public boolean groupSum(int start, int[] nums, int target) { //Aux excercise 5
        boolean add; //c10
        boolean add_not = false; //c11
        if(start >= nums.length){ //c12
            return target == 0; //c13
        }
        add = groupSum(start +1, nums, target - nums[start]); // G(n-1) + c14
        add_not = groupSum(start +1, nums, target); //G(n-1) + c15
        return add || add_not; //c16
    }
    //we get
    //G(n) = c10 + c11 + c12 + c13 if n == 0
    //worst case:
    // G(n) = G(n-1) + G(n-1)+ C = C*((2**n)-1) + c18*2**n-1
    //then
    //G(n) = O(2**n) with n being the lenght of nums 
}

