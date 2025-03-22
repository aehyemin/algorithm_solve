var sumOfUnique = function(nums) {
    let ans = 0
    let has = {}
    for (let num of nums){
        if (!(num in has)) {
            has[num] = 1
        } else {
            has[num] += 1
        }
    }   
    for (let key in has) {
        if(has[key] == 1) {
            ans += Number(key)
        }
    }
    return ans
}