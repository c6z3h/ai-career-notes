class Solution {
    public boolean isPowerOfThree(int n) {
    /*    float var = n;
        while (var>2){
            var = var/3;
        }
        System.out.println(var);
        if (var == 1){return true;}
        else return false;
    }*/
        // This Quicker Method as Float Method Above Gives Rounding Error.
        return ( n>0 &&  1162261467%n==0);}
        
}
