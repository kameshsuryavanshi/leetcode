class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        int c=0;
        for(int i=0;i<nums.length;i++){
                if(nums[i] != nums[c]){
                    c++;
                   nums[c] = nums[i];                   
                }
            }
            
        return c+1;
    }   
    
}