class Solution {
    public boolean isPowerOfThree(int n) {
        while (n>2){
            n = n/3;
        }
        if (n == 1){return true;}
        else return false;
    }
}
