int differenceOfSum(int* nums, int numsSize) {
     int elemsum=0;
        int digitsum=0;
        for (int i=0;i<numsSize ; i++){
            int num=nums[i];
            elemsum+=num;
            while (num!=0){
                int dig=num%10;
                digitsum+=dig;
                num=num/10;
            }}
        return elemsum-digitsum;
    
}