int thirdMax(int* nums, int numsSize) {
    int max[3]; // 0 is max, 1 is second, 2 is third
    max[0] = INT_MIN;
    max[1] = INT_MIN;
    max[2] = INT_MIN;
    int times = -1;
    bool first_min = true;
    for (int i = 0; i < numsSize; i++) {
        bool dup = false;
        for (int j = 0; j < 3; j++){
            if (nums[i] == INT_MIN && first_min) {
                times ++;
                first_min = false; 
            }
            else if (max[j] == nums[i]) {
                dup = true;
            }
        }
        if (dup) {
            continue;
        }
        if (nums[i] > max[0]) {
            max[2] = max[1];
            max[1] = max[0];
            max[0] = nums[i];
            times += 1;
        } else if (nums[i] > max[1]) {
            max[2] = max[1];
            max[1] = nums[i];
            times += 1;
        } else if (nums[i] > max[2]) {
            max[2] = nums[i];
            times += 1;
        }
    }
    return times < 2 ? max[0] : max[2];
}
