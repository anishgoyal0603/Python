class Solution {
    public int rotatedDigits(int n) {
        // dp[i] will store the state of the number 'i'
        // 0 = Invalid, 1 = Valid but same, 2 = Good
        int[] dp = new int[n + 1];
        int count = 0;
        
        for (int i = 0; i <= n; i++) {
            // Base cases for single digits
            if (i < 10) {
                if (i == 0 || i == 1 || i == 8) {
                    dp[i] = 1;
                } else if (i == 2 || i == 5 || i == 6 || i == 9) {
                    dp[i] = 2;
                    count++;
                }
            } 
            // For numbers >= 10, derive state from previously calculated smaller numbers
            else {
                int a = dp[i / 10]; // State of all digits except the last one
                int b = dp[i % 10]; // State of the last digit
                
                // If either part is invalid, the whole number is invalid (dp[i] remains 0)
                
                // If both parts are valid-but-same, the whole number is valid-but-same
                if (a == 1 && b == 1) {
                    dp[i] = 1;
                } 
                // If both parts are valid, and AT LEAST ONE part is "good" (2), the whole number is good
                else if (a >= 1 && b >= 1) {
                    dp[i] = 2;
                    count++;
                }
            }
        }
        
        return count;
    }
}