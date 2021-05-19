class Solution {
    public int removeDuplicates(int[] nums) {
        /*
        Question May Be Poorly Worded.
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == nums[i+1]){
                for (int j = i+1; j < (nums.length - i - 1); j++){
                    nums[j] = nums[j+1];
                }
            }
        }
        System.out.println(nums);
        return nums.length;*/
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}
