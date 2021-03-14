
public class Array3
{
    public int maxSpan(int[] nums) { //exercie 1 c0
        int comp = 0;//c1
        int max = 0;//c2
        while(comp < nums.length ){//n*c3
            for(int i = nums.length -1; i >= 0; i--){//n*n*c4
                if(nums[i] == nums[comp] && max < i - comp + 1){//n*n*c5
                    max = i - comp +1;//n*c6
                    break;//n*c7
                }
                else if(i == 0 && max < i - comp + 1){//n*n*c8
                    max = 1;//n*n*c9
                }
            }
            comp ++;//n*c10
        }
        return max;//c11

    }
    //we get
    //T(n) = c0 + c1 + c2 + n*c3 + n*n*c4 + n*n*c8 + n*n*c9 + n*c10 + c11
    //then
    //T(n) = O(n**2) with n length of nums

    public int[] fix34(int[] nums) { //exercise 2 c0
        int temp = 0; //c1
        for(int i = 0; i < nums.length; i++){//n*c2
            if(nums[i] == 3){//n*c3
                for(int j = 0; j< nums.length; j++){//n*n*c4
                    if(nums[j] == 4 && nums[j-1] != 3){//n*n*c5
                        temp = nums[i+1];//n*c6
                        nums[i+1] = nums[j];//n*c7
                        nums[j] = temp;//n*c8
                        break;//n*c9
                    }
                }
            }
        }
        return nums;//c10
    }
    //we get
    //T(n) = c0 + c1 + n*c2 + n*c3 + n*n*c4 + n*n*c5 + c10 
    //then
    //T(n) = O(n**2) with n length of nums

    public int[] fix45(int[] nums) { //exercise 3 c0
        int temp = 0;//c1
        for(int i = 0; i < nums.length; i++){//n*c2
            if(nums[i] == 4){//n*c3
                for(int j = 0; j< nums.length; j++){//n*n*c4
                    if(nums[j] == 5 && (j == 0 || nums[j-1] != 4 )){//n*n*c5
                        temp = nums[i+1];//n*c6
                        nums[i+1] = nums[j];//n*c7
                        nums[j] = temp;//n*c8
                        break;//n*c9
                    }
                }
            }
        }
        return nums;//c10
    }
    //we get
    //T(n) = c0 + c1 + n*c2 + n*c3 + n*n*c4 + n*n*c5 + c10 
    //then
    //T(n) = O(n**2) with n length of nums

    public boolean canBalance(int[] nums) { //exercise 4 c0
        int sum = 0;//c1
        for (int i = 0; i < nums.length; i++){//n*c2
            sum = sum + nums[i];//n*c3
        }
        if(sum%2 != 0){//c4
            return false;//c5
        }
        int objective = sum/2;//c6
        sum = 0;//c7
        for(int j = 0; j < nums.length; j++){//n*c8
            sum = sum + nums[j];//n*c9
            if(sum == objective){//n*c10
                return true;//c11
            }
        }
        return false;//c12
    }
    //we get
    //T(n) = c0 + c1 + n*c2 + n*c3 + c4 + c6 + c7 + n*c8 + c*c9 + c*c10 + c12
    //then
    //T(n) = O(n) with n length of nums

    public boolean linearIn(int[] outer, int[] inner) { // exercise 5 c0
        int i = 0; //c1
        int j = 0; //c2
        int count = 0; //c3
        while(i < outer.length && j < inner.length){ //n*c4
            if(outer[i] <= inner[j]){//n*c5
                if(outer[i] == inner[j]){//n*c6
                    count++;//n*c7
                    j++;//n*c8
                }
            }
            else{//c9
                return false;//c10
            }
            i++;//n*c11
        }
        return count >= inner.length;//c12
    }
    //we get
    //T(n) = c0 + c1 + n*c2 + c3 + n*c4 + n*c5 + n*c6 + n*c11 + c12 
    //then
    //T(n) = O(n) with n length of outer
    //Note, we assume that either inner has the same length of outer or the element matches for inner are located
    //in the very last positions of outer, such that the whole array outer must be evaluated
}