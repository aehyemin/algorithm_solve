/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    let hash = {}
    let ans = 0
    
    for(let i of nums) {
        hash[i] = (hash[i] || 0) + 1
    }

    max_val = Math.max(...Object.values(hash))
   

    for(let key in hash) {
        if (hash[key] == max_val) {
            ans += max_val
        }       
    }
    return ans
};