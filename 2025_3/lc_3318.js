/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
function getTopX(hash, x) {
    let sorted = Object.entries(hash)
        .map(([key, value]) => [parseInt(key), value])    
        .sort((a,b) => b[1] - a[1] || b[0] - a[0])
    return sorted.slice(0, x).reduce((acc, entry) => acc + entry[0] * entry[1], 0);
    }
var findXSum = function(nums, k, x) {
    //top x 의 합계를 구하는 함수
    
    let hash = {}
    let ans = []
    let k_num = nums.slice(0,k)
    console.log(k_num)

    for(let num of k_num) {
        hash[num] = (hash[num] || 0) + 1;
    }

    ans.push(getTopX(hash, x));

    for (let j=k; j<nums.length; j++) {
        let oldNum = nums[j-k]
        let newNum = nums[j]

        hash[oldNum] -= 1
        if (hash[oldNum] == 0) {
            delete hash[oldNum]
        }

        hash[newNum] = (hash[newNum] || 0) + 1;
        ans.push(getTopX(hash, x));
    }

    return ans
  
};