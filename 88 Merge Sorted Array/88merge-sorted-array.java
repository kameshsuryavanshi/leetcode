class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int a = m - 1;
        int b = n - 1;
        int c = m + n - 1; // Corrected initialization

        while (a >= 0 && b >= 0) {
            if (nums1[a] < nums2[b]) {
                nums1[c--] = nums2[b--];
            } else {
                nums1[c--] = nums1[a--];
            }
        }

        while (b >= 0) { // Handling remaining elements from nums2
            nums1[c--] = nums2[b--];
        }
    }
}
