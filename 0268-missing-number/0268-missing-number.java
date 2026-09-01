class Solution {
    public int missingNumber(int[] nums) {
        int sum=0;
        int n =nums.length;
        int actualsum=(n*(n+1))/2;
        for (int i=0 ; i<n ; i++){
            sum+=nums[i];
        }
        int missing = actualsum-sum;
        return missing;
    }
}


//         Arrays.sort(nums);
//         int n =nums.length;
//         for (int i=0 ; i<n ;i++){
//             if(nums[i] != i){
//                 return i;
//             }
//         }
//         return n;   
//     }
// }