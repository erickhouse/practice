

/**
 * 
 * @param {number[]} arr 
 * @description selection sort scans the unsorted part of the array while insertion sort scans the sorted part of the array.
 * the j loop will go out of bounds by one index at the end which will return undefined.
 * An undefined compared against an numeric value always returns false.
 */
function selectionSort(arr) {
    for(let i = 0; i < arr.length; i++) {
        let min = i;
        for(let j = i + 1; j < arr.length; j++) {
            if(arr[j] < arr[min]) {
                min = j;
            }
        }
        [arr[i], arr[min]] = [arr[min], arr[i]];
    }
    return arr;
}

/**
 * 
 * @param {number[]} arr 
 * @description on a completely sorted array the runtime is only O(n) given that is only has to inspect the element to its left.
 * Selction sort always has to scan the rest of the array to find the absolute minium.
 */
function insertionSort(arr) {
    for(let i = 0; i < arr.length; i++) {
        for(let j = i; j >= 0; j--) {            
            if(arr[j] < arr[j-1]) {
                [arr[j-1], arr[j]] = [arr[j], arr[j-1]];
            }else{
                break;
            }
        }
    }
    return arr;
}

/**
 * @param {number[]} arr 
 * @description typically insertion sort is better than bubble sort but they both have the same worst case runtime of O(n^2). 
 * There might be a case if the array is almost sorted. The largest number will bubble to the end of the array after each iteration and
 * we know the array is sorted until that point.
 */
function bubbleSort(arr) {
    let n = arr.length;
    for(let i = n-1; i > 0; i--) {
        for(let j = 0; j < i; j++) {
            if(arr[j] > arr[j+1]){
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
            }
        }
    }
    return arr;
}
