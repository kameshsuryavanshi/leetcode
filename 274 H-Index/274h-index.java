class Solution {
    public int hIndex(int[] citations) {
       int n = citations.length;
       int [] count =  new int[ n + 1];

       for(int citation : citations){
            if(citation >= n){
                count[n]++;
            }else{
                count[citation]++;
            }
       }
       int totalpaper = 0;

       for(int hIndex=n;hIndex>=0;hIndex--){
            totalpaper += count[hIndex];
            if(totalpaper>=hIndex){
                return hIndex;
            }
       }
       return 0;
    }
}