//Copyright 2023 Chris/abstractedfox.
//This work is not licensed for use as source or training data for any language model, neural network,
//AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
//new or derived content from or based on the input set, or used to build a data set or training model for any software or
//tooling which facilitates the use or operation of such software.

//ok, here it is, the ultimate solution, no way to lose:
//starting from the second to last element (0-indexed end - 2), determine whether taking the next step or skipping that step is cheaper. Save this to a dictionary as (index, value).
//For each next element toward 0, do the following: Check the value of that index + the dictionary matched value of the next two indexes. Whichever one is cheaper, create a new dictionary entry for this index and advance.

public class Solution {
    public int LetsUseADictionary(int[] cost){
        Dictionary<int, int> perIndexResults = new Dictionary<int, int>();

        perIndexResults.Add(cost.Length - 1, cost[cost.Length - 1]);
        perIndexResults.Add(cost.Length - 2, cost[cost.Length - 2]);

        for (int i = cost.Length - 3; i >= 0; --i){
            if (cost[i] + perIndexResults[i + 1] < cost[i] + perIndexResults[i + 2]){
                perIndexResults.Add(i, cost[i] + perIndexResults[i+1]);
                continue;
            }

            perIndexResults.Add(i, cost[i] + perIndexResults[i + 2]);
        }

        if (perIndexResults[1] < perIndexResults[0]){
            return perIndexResults[1];
        }

        return perIndexResults[0];
    }

    public int MinCostClimbingStairs(int[] cost) {
        return LetsUseADictionary(cost);
    }
}