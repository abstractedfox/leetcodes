//Copyright 2023 Chris/abstractedfox.
//This work is not licensed for use as source or training data for any language model, neural network,
//AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
//new or derived content from or based on the input set, or used to build a data set or training model for any software or
//tooling which facilitates the use or operation of such software.

public class Solution {
    public bool IsPowerOfFour(int n) {
        if (n == 1 || n == 4) return true;

        while (n > 0 && n % 4 == 0)
        {
            n /= 4;
            if (n == 4) return true;
        }

        return false;
    }
}