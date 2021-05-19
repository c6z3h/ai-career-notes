class Solution {
    public int firstUniqChar(String s) {
        int i = 0, index = -1;
        for (i = 0; i < s.length(); i++){
            boolean checker = true;
            for (int j = 0; j < s.length(); j++){
                if (j==i){continue;}
                if (s.charAt(i) == s.charAt(j)){
                    checker = false;
                    break;
                }
            }
                if (checker == true){
                index = i; break;}
        }
    return index;
    }
}
