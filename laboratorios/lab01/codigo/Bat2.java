
public class Bat2
{
    public boolean groupSum(int start, int[] nums, int target) { //base
        boolean add;
        boolean add_not = false;
        if(start >= nums.length){
            return target == 0;
        }
        add = groupSum(start +1, nums, target - nums[start]);
        add_not = groupSum(start +1, nums, target);
        return add || add_not;
    }

    public boolean groupSum6(int start, int[] nums, int target) { //excersie 1
        boolean add;
        boolean add_not = false;
        if(start >= nums.length){
            return target == 0;
        }
        if(nums[start] == 6){
            add = groupSum6(start +1, nums, target - nums[start]);
        }
        else{
            add = groupSum6(start +1, nums, target - nums[start]);
            add_not = groupSum6(start +1, nums, target);
        }
        return add || add_not;
    }

    public boolean groupNoAdj(int start, int[] nums, int target)  { //excersie 2
        boolean add;
        boolean add_not = false;
        if(start >= nums.length){
            return target == 0;
        }
        add = groupNoAdj(start +2, nums, target - nums[start]);
        add_not = groupNoAdj(start +1, nums, target);
        return add || add_not;
    }

    public boolean groupSum5(int start, int[] nums, int target) { //excersie 3
        boolean add = false;
        boolean add_not = false;

        if(start >= nums.length){
            return target == 0;
        }

        if(nums[start]%5 == 0){
            add = groupSum5(start +1, nums, target - nums[start]);
        }
        else if(start != 0 && nums[start -1] == 5 && nums[start] == 1){
            add_not = groupSum5(start +1, nums, target);
        }
        else{
            add = groupSum5(start +1, nums, target - nums[start]);
            add_not = groupSum5(start +1, nums, target);
        }
        return add || add_not;
    }

    public boolean groupSumClump(int start, int[] nums, int target) { //excersie 4
        boolean add = false;
        boolean add_not = false;
        if(start >= nums.length){
            return target == 0;
        }

        if(start-1 != -1 && nums[start-1] == nums[start] ){
            add= groupSumClump(start +1, nums, target - nums[start]);
            add_not = groupSumClump(start +1, nums, target + nums[start]);
        }
        else if(start+1 != nums.length && nums[start+1] == nums[start] ){
            add= groupSumClump(start +1, nums, target - nums[start]);
            add_not = groupSumClump(start +1, nums, target + nums[start]);
        }
        else{
            add =groupSumClump(start +1, nums, target - nums[start]);
            add_not = groupSumClump(start +1, nums, target);
        }
        return  add || add_not;
    }

    public boolean splitArray(int[] nums) { //excercise 5
        int n = sumArray(nums,nums.length);
        if(n%2 != 0){
            return false;
        }
        return groupSum(0, nums, n/2);
        }
    
    public int sumArray(int[] nums, int n){
        if(n <= 0){
            return 0;
        }
        return sumArray(nums, n - 1) + nums[n - 1]; 
    }
}
