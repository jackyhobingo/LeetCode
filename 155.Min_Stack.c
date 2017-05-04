typedef struct {
    int *arr;
    int *min_arr;
    int min_top;
    int maxSize;
    int top;
} MinStack;

/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack *minStack = (MinStack *) malloc(sizeof(MinStack));
    minStack->maxSize = maxSize;
    minStack->arr = (int *) malloc(sizeof(int) * maxSize);
    minStack->min_arr = (int *) malloc(sizeof(int) * maxSize);
    minStack->top = -1;
    minStack->min_top = -1;
    return minStack;
}

void minStackPush(MinStack* obj, int x) {
    if (obj->min_top < 0 || obj->min_arr[obj->min_top] >= x) {
        obj->min_arr[++(obj->min_top)] = x;
    }
    obj->arr[++(obj->top)] = x;
}

void minStackPop(MinStack* obj) {
    
    if (obj->min_arr[obj->min_top] == obj->arr[obj->top]) {
        obj->min_top --;
    }
    obj->top --;
}

int minStackTop(MinStack* obj) {
    return obj->arr[obj->top];
}

int minStackGetMin(MinStack* obj) {
    return obj->min_arr[obj->min_top];
}

void minStackFree(MinStack* obj) {
    free(obj->arr);
    free(obj->min_arr);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */
