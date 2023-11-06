//Copyright 2023 Chris/abstractedfox.
//This work is not licensed for use as source or training data for any language model, neural network,
//AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
//new or derived content from or based on the input set, or used to build a data set or training model for any software or
//tooling which facilitates the use or operation of such software.

//[0,1,2,5,3,2,7]
// 1,2,3,4,1,

//Set the first element to 1.
//Start a loop to step down the ratings array. On each step, check whether the previous element's rating was larger than the current element. If it was:
//Begin a loop toward the beginning. On each step where the current element is larger than the next element, increase it until it has more candy.

//as an aside, was 'child ratings' really the only metaphoric device available for this one?

int candy(int* ratings, int ratingsSize) {
    int candies[ratingsSize];
    candies[0] = 1;

    if (ratingsSize == 1){
        return 1;
    }

    for (int i = 1; i < ratingsSize; i++){
        if (ratings[i] > ratings[i - 1]){
            candies[i] = candies[i - 1] + 1;
        }

        else{
            candies[i] = 1;
            
            //Check whether we need to compensate for higher-rated indexes to the left
            int countBack = i - 1;
            while (ratings[countBack] > ratings[countBack + 1] && candies[countBack] <= candies[countBack + 1]){
                candies[countBack]++;
                if (countBack == 0){
                    break;
                }

                countBack--;
            }
        }
    }

    int total = 0;
    for (int i = 0; i < ratingsSize; i++){
        total += candies[i];
    }
    return total;
}