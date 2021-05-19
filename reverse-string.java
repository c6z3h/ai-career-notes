class Solution {
    public void reverseString(char[] s) {
        // 2. Then Reverse the Entire String
        for (int i = 0; i < (int) s.length / 2; i++){
            // 1. Store Precedent Letter in char Variable
            char letterStore = s[i];
            s[i] = s[s.length-i-1];
            // 3. Then Put the Stored Letter into Rear Position
            s[s.length-i-1] = letterStore;
        }
    }
}
