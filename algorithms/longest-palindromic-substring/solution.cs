//Copyright 2023 Chris/abstractedfox.
//This work is not licensed for use as source or training data for any language model, neural network,
//AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
//new or derived content from or based on the input set, or used to build a data set or training model for any software or
//tooling which facilitates the use or operation of such software.

public class Solution {
    public string LongestPalindrome(string s) {
        string favorite = s[0].ToString();

        for (int i = 0; i < s.Length; i++){
            if (s.Length - i < favorite.Length) break;

            for (int j = s.Length - 1; j > i; j--){
                if ((j - i) < favorite.Length) break;

                string compare = isPalindrome(s.Substring(i, j + 1 - i));
                if (compare.Length > favorite.Length) favorite = compare;
            }
        }

        return favorite;
    }

    public string isPalindrome(string s){
        for (int i = 0; i < s.Length; i++){
            if (i == s.Length - 1 - i) break;
            if (s[i] != s[s.Length - 1 - i]) return "";
        }
        return s;
    }
    
}