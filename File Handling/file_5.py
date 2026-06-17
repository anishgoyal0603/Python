class Solution {
    public char processStr(String s, long k) {
        int n = s.length();
        long[] len = new long[n];
        long currentLen = 0;
        
        // Step 1: Forward pass just to compute the simulated lengths
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '*') {
                currentLen = Math.max(0, currentLen - 1);
            } else if (c == '#') {
                currentLen *= 2;
            } else if (c == '%') {
                // Length does not change
            } else {
                currentLen += 1;
            }
            len[i] = currentLen;
        }
        
        // Bounds check
        if (k < 0 || k >= currentLen) {
            return '.';
        }
        
        // Step 2: Backward pass (Time Travel) to track the origin of index k
        long idx = k;
        for (int i = n - 1; i >= 0; i--) {
            char c = s.charAt(i);
            
            // L is the length of the string right before the current operation
            long L = (i == 0) ? 0 : len[i - 1];
            
            if (c == '*') {
                // The removed character was at the end, our tracking index is unaffected
                continue;
            } else if (c == '#') {
                // If our index came from the duplicated second half, shift it to the first half
                if (idx >= L) {
                    idx -= L;
                }
            } else if (c == '%') {
                // The string was reversed, so our index mirrors to the opposite side
                idx = L - 1 - idx;
            } else {
                // It's a standard letter. Was it placed exactly at our current tracking index?
                if (idx == L) {
                    return c;
                }
            }
        }
        
        return '.';
    }
}