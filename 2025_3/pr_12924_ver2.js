function solution(n) {
    let ans = 0
    for(let i=1; i<(n+1); i++) {
        let total = 0;
        for(let j=i; j< n + 1; j++) {
            total += j
            
            if (total == n) {
                ans += 1
                break
            } else if (total > n) {
                break
            }
                
        }
    }
    return ans
}