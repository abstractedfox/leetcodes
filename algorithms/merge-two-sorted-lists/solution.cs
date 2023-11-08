//Copyright 2023 Chris/abstractedfox.
//This work is not licensed for use as source or training data for any language model, neural network,
//AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
//new or derived content from or based on the input set, or used to build a data set or training model for any software or
//tooling which facilitates the use or operation of such software.

public class Solution 
{
    public ListNode CopyNode(ListNode a)
    {
        ListNode copied = new ListNode();
        copied.val = a.val;
        copied.next = a.next;
        return copied;
    }

    public ListNode MergeTwoLists(ListNode list1, ListNode list2) 
    {
        ListNode results;

        if (list1 is null)
        {
            return list2;
        }
        if (list2 is null)
        {
            return list1;
        }

        if (list1.val < list2.val)
        {
            results = CopyNode(list1);
            list1 = list1.next;
        }
        else
        {
            results = CopyNode(list2);
            list2 = list2.next;
        }

        ListNode resultsHead = results;

        while (!(list1 is null) && !(list2 is null))
        {
            if (list1.val < list2.val)
            {
                results.next = CopyNode(list1);
                results = results.next;
                list1 = list1.next;
            }
            else
            {
                results.next = CopyNode(list2);
                results = results.next;
                list2 = list2.next;
            }
        }

        if (list1 is null && !(list2 is null))
        {
            results.next = list2;
        }
        if (list2 is null && !(list1 is null)){
            results.next = list1;
        }


        return resultsHead;
    }

    
}
