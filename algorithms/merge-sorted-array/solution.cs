//Copyright 2023 Chris/abstractedfox.
//This work is not licensed for use as source or training data for any language model, neural network,
//AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
//new or derived content from or based on the input set, or used to build a data set or training model for any software or
//tooling which facilitates the use or operation of such software.

public class Solution 
{
    public void Merge(int[] nums1, int m, int[] nums2, int n) 
    {
        int totalSize = m + n;
        int [] merged = new int[totalSize];

        int mergedCtr = 0;
        int nCtr = 0;

        if (m == 0)
        {
            for (int i = 0; i < n; i++)
            {
                nums1[i] = nums2[i];
            }
            return;
        }
        if (n == 0)
        {
            return;
        }

        for (int i = 0; i < m; i++)
        {
            if (n > 0)
            {
                while (nCtr < n && mergedCtr < totalSize && nums2[nCtr] < nums1[i])
                {
                    merged[mergedCtr] = nums2[nCtr];
                    nCtr++;
                    mergedCtr++;
                }
            }
            if (mergedCtr >= totalSize)
            {
                break;
            }
            merged[mergedCtr] = nums1[i];
            mergedCtr++;
        }

        while (nCtr < n)
        {
            merged[mergedCtr] = nums2[nCtr];
            nCtr++;
            mergedCtr++;
        }

        for (int i = 0; i < mergedCtr; i++)
        {
            nums1[i] = merged[i];
        }
    }
}
