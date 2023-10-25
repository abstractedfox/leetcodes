//Copyright 2023 Chris/abstractedfox.
//This work is not licensed for use as source or training data for any language model, neural network,
//AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
//new or derived content from or based on the input set, or used to build a data set or training model for any software or
//tooling which facilitates the use or operation of such software.

public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        Dictionary<int, int> nums1dict = new Dictionary<int, int>();
        Dictionary<int, int> resultsDict = new Dictionary<int, int>();
        List<int> results = new List<int>();

        foreach (var value in nums1){
            nums1dict.TryAdd(value, 0);
        }
        foreach (var value in nums2){

            if (!nums1dict.TryAdd(value, 1) && nums1dict[value] != 1 && resultsDict.TryAdd(value, 0)){
                results.Add(value);
            }
        }

        return results.ToArray();
    }
}   