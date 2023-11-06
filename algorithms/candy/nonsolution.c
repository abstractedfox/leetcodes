//Copyright 2023 Chris/abstractedfox.
//This work is not licensed for use as source or training data for any language model, neural network,
//AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
//new or derived content from or based on the input set, or used to build a data set or training model for any software or
//tooling which facilitates the use or operation of such software.

//Worth noting: The rating does not inform the number of candies directly, it only informs whether that one should receive more than their neighbors

//On each increment:
//Initialize the current index to '1'.
//Check the element to the left. If it has a lower rating than the current element, set the current element to that element + 1.
//If the previous element is greater than the current element: Begin a new loop iterating backward
//actually wait, i feel like this can be done on one iteration

//let's think of some tricky cases
//first row being the 'ratings' and second row being our potential output:
// 1, 1, 1, 1, 2, 3, 2, 1, 4, 3, 1 (ratings)
// 1, 1, 1, 1, 2, 3, 2, 1, 3, 2, 1 (correct output)
// 1, 2, 3, 4, 6, 9,11,12,15,17,18 (running count per step)
//rate of change of candies given per step:
//+1 +0 +0 +0 +1 +1 -1 -1 +2 -1 -1
//but we could also say:
//if the current element is bigger than the previous element, the change in number of candies awarded should increment by 1
//if the current element is smaller than the previous element, the change in number of candies awarded should decrement by 1

//thinking out loud (in text?)
//from 1 we reach 4, increasing the rate of change by 1, making the total 14 (this value will be incorrect soon but we don't know that looking just at 4)
//from 4 we reach 3, decreasing the rate of change back to 1, making the total 15
//from 3 we reach 1, the rate of change can not decrease below 1, but:
//we can say that this means each element since the last time we noticed [the rating value goes down, then increases] must increase by 1 for every element we have iterated since then
//so this would mean we owe one to the total for each element we have iterated over since then, which is three. this would give us the correct total of 18
//lastly, what does this do to our running rate of change if we exit this circumstance, since the rate of change can't go below 1?
//let's alter that problem set from above:
// 1, 1, 1, 1, 2, 3, 2, 1, 5, 4, 2, 1, 2 (ratings)
// 1, 1, 1, 1, 2, 3, 2, 1, 4, 3, 2, 1, 2 (correct output)
// 1, 2, 3, 4, 6, 9,11,12,16,19,21,22,24 (running count per step)

//and consider the algorithm we just imagined:
//starting with the count at 1 on element 1 (0 indexed), the previous element is the same, so increase the count by 1 for a total of 2
//do this again for [2], total of 3
//again for [3], total of 4
//[4] the rating has increased, increase the rate of change by 1, for a change of 2, total of 6
//[5] the rating has increased, increase the rate of change by 1, for a change of 3, total of 9
//[6] the rating has decreased, decrease the rate of change by 1, for a change of 2, total of 11
//[7] the rating has decreased, decrease the rate of change by 1, for a change of 1, total of 12
//[8] the rating has increased, increase the rate of change by 1, for a change of 2, total of 14
//[9] 

//actually you know what, i just realized something: i think we can just say that any time we are counting down rate of change following a low-to-high change, for each subsequent attempt to decrease the rate of change below 1, we make the rate of change the number of indexes since the highest value we're counting down from, plus one. let's think about this again, just starting from there:
//[7] the rating has decreased, decrease the rate of change by 1, for a change of 1, total of 12
//[8] the rating has increased, increase the rate of change by 1, for a change of 2, total of 14
//[9] the rating has decreased, decrease the rate of change by 1, for a change of 1, total of 15. save the index of 8 to a variable 'countdown'
//[10] the rating has decreased, decrease the rate of change by 1. the change cannot go below 1, so the rate of change becomes 10-countdown + 1, which is 3, for a total of 18.
//[11] the behavior from [10] repeats; the rate of change becomes 11-countdown + 1 which is 4, for a total of 22
//[12] the rating has increased, the rate of change increases by 1, for a change of 2, total of 24
//boom!!!


//problem case (getting 9 and should be getting 7):
//[ 1, 3, 2, 2, 1] (should return 7)
//[ 1, 2, 1, 2, 1] (correct rate of change per element)
//[ 1, 3, 4, 6, 7] (running totals)
//so we missed something; adjacent values that are the same can be given different candy values. our algorithm is returning 9 because when it's hitting its countdown case when it hits [4].
//what it actually needs to do is: when the rate of change tries to go below 1, and the previous elements two are the same, use the countdown case but with countdown set to the previous element

//new problem case:
//[ 29, 51, 87, 87, 72, 12] (should return 12, is returning 11)
//[  1,  2,  3,  2,  1, (1 + 2)] (the correct rate of change that we want, adds up to 12)
//[  1,  3,  6,  8,  9, 12] (running total)
//oh I see, the edge case we added for 'two consecutive elements' was in the else block (i wonder who did that)

//if you can believe it it's a problem case once again!
//[ 1, 2,87,87,87, 2, 1] (should be 13, getting 14)
//[ 1, 2, 3, 1, 3, 2, 1] (I see; cases where a value is bordered only by itself should always be 1. )

//again!
//[ 1, 3, 4, 5, 2] (returning 13, should return 11)
//[ 1, 2, 3, 4, 1] (correct rate of change per element)
//We haven't considered cases where the last element is smaller than its only neighbor, meaning it can clamp directly to 1

//back at it again at krispy kreme!
//[ 0, 1, 2, 3, 2, 1] (should get 14, we're getting 13)
//[ 1, 2, 3, 4, 2, 1] (correct rate of change per element, adds up to 14)
//the problem is that [4] should go down to 2 and it's currently going to 3.
//how can we define this case? an element which is smaller than the previous element (2 < 3), where the rate of change of the previous iteration is greater than the current element + 1, can be clamped to 1

//more!!!!
//[ 0, 1, 2, 5, 3, 2, 7] (should be 15, getting 18)
//[ 1, 2, 3, 4, 2, 1, 2] (correct rate of change per element)
//[ 1, 3, 6,10,12,13,15] (running total)

int candy(int* ratings, int ratingsSize) {
    int countdown = 0; //also a great disco song by dan hartman
    int rateOfChange = 1;
    int total = 1; //the loop begins at index [1], so we need to count at least 1 candy for index [0]
    int candyArr[ratingsSize];
    candyArr[0] = 1;
    
    if (ratingsSize == 1){
        return 1;
    }

    for (int i = 1; i < ratingsSize; i++){
        //Element is only bordered by the same value
        if (i < ratingsSize - 1 && i > 0){
            if (ratings[i - 1] == ratings[i] && ratings[i] == ratings[i + 1]){
                rateOfChange = 1;
                total += rateOfChange;
                continue;
            }
        }

        if (ratings[i] > ratings[i - 1]){
            printf("Setting countdown! i = %d\n", i);
            rateOfChange += 1;
            countdown = i;
        }

        if (ratings[i] == ratings[i - 1] && rateOfChange > 1){
            rateOfChange--;
        }

        if (ratings[i] < ratings[i - 1]){
            //printf("at i[%d], the value %d is smaller than the previous element %d\n", i, ratings[i], ratings[i - 1]);

            //The rate of change is greater than the the current element + 1
            if (rateOfChange > ratings[i] + 1){
                printf("The rate of change is greater than the current element");
                rateOfChange = 1;
                total += rateOfChange;
                countdown = i;
                printf("i[%d] Added rateofchange %d for a total of %d\n",i,  rateOfChange, total);
                continue;
            }

            //case: the previous two elements are the same
            if (i > 2){
                //printf("on element %d, previous two elements are %d,%d\n", i, ratings[i - 1], ratings[i - 2]);
                if (ratings[i - 1] == ratings[i - 2]){
                    printf("Previous two elements are the same and rating[i] is smaller. i = %d", i);
                    countdown = i - 1;
                }
            }

            if (rateOfChange > 1){
                //It's the last element, there is no 'countdown' deficit, and the previous element is bigger,
                //so we can clamp the rate of change to 1.
                if (i == ratingsSize - 1){
                    printf("Last element clamping to 1 case, total is %d\n", total);
                    total++;
                    printf("Clamped total is %d", total);
                    break;
                }

                //rateOfChange--;
                rateOfChange = 1;
            }

            else{
                printf("Countdown case! countdown value: %d i: %d total: %d\n", countdown, i, total);
                total += i - countdown + 1;
                printf("i[%d] Added rateofchange %d for a total of %d\n",i,  rateOfChange, total);
                continue;
            }
        }
        total += rateOfChange;
        printf("i[%d] Added rateofchange %d for a total of %d\n",i,  rateOfChange, total);
    }

    return total;
}
