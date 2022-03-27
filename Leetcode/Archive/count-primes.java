// Seems Default Boolean is Assigned False.
// My Method (Commented Out) is Computationally Slow.
/*
class Solution {
    public int countPrimes(int n) {
        //Count the number of prime numbers less than a non-negative number, n.
        //Prime numbers are divisible only by the number 1 or itself.
        int counter = 0;
        for (n = n-1; n>1; n--){
            boolean prime = true;
            for (int check = n-1; check>1; check--){
                if ((float)n/check == n/check){
                    prime = false;
                    break;
                } 
            }
            if (prime == true){counter +=1;}
        }
    return counter;
    }
}
*/
public class Solution {
    public int countPrimes(int n) {
        boolean[] notPrime = new boolean[n];
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (notPrime[i] == false) {
                count++;
                for (int j = 2; i*j < n; j++) {
                    notPrime[i*j] = true;
                }
            }
        }
        
        return count;
    }
}
