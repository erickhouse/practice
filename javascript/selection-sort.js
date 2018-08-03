
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
