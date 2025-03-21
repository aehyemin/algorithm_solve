function solution(n) {
    let ans=0
    let total=0
    let left = 0
    for(let i=1; i<=n; i++) {
        total += i
        
        while (total > n){
            total -= left
            left +=1
        }
        
        if (total==n) {
            ans += 1
        }
        
    }
    return ans
}