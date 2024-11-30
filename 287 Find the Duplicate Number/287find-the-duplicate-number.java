class Solution {
    public int findDuplicate(int[] arr) {
        
        int n = arr.length;
        int newarr[] = new int[n+1];
        //  Arrays.sort(arr);
        for(int i=0;i<n ; i++){
            if(newarr[arr[i]] == 0){
                 newarr[arr[i]] +=1;
            }else{
                return arr[i];
            }
        }
        return 0;
    }
}