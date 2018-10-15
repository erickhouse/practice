
/**
 * Creates all combinations of all numbers in the Set
 * It doesn this this through iterations instead of the traditional 
 * recursive method
 * @param {Set<number>} arr 
 * @returns {Set<Set<number>>}
 */
function iterateCombinations(arr) {

    let results = new Set([[]]);
    for(let i of arr) {
        let temp = [...results];
        for(let j of temp) {
            results.add([i, ...j]);
        }
    }
    return results;
}
