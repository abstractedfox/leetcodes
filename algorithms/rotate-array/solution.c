//Create a new array that is the same length as the input array.
//For each character in the input array:
//If the index of that character + k + i < length(input), copy that character to that index in the new array.
//If it is greater than length(input), copy the character to ((i + k) % length(input))

void rotate(int* nums, int numsSize, int k) {
    int rotated[numsSize];
    for (int i = 0; i < numsSize; i++){
        printf("num! %d\n", nums[i]);
        if (i + k < numsSize){
            rotated[i + k] = nums[i];
        }
        else{
            rotated[(i + k) % numsSize] = nums[i];
            
        }
    }

    for (int i = 0; i < numsSize; i++){
        nums[i] = rotated[i];
    }
    nums = &rotated;
}