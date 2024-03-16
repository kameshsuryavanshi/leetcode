class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];

        int leftProduct = 1;
        for(int i=0;i<n;i++){
            arr[i] = leftProduct;
            leftProduct *= nums[i] ; 
        }
        int rightProduct = 1;
        for(int i=n-1;i>=0;i--){
            arr[i] *=  rightProduct ;
            rightProduct *= nums[i];
        }
        return arr;
    }
}