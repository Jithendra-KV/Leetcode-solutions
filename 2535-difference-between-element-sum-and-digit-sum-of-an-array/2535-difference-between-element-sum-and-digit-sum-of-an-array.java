class Solution {
    public int differenceOfSum(int[] nums) {
        int elemsum=0;
        int digitsum=0;
        for (int num : nums){
            elemsum+=num;
            while (num!=0){
                int dig=num%10;
                digitsum+=dig;
                num=num/10;
            }}
        return elemsum-digitsum;

    }
}