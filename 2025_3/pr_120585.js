function solution(array, height) {
    var cnt = 0
    for(i=0; i<array.length; i++) {
        if (height < array[i]) {
            cnt+=1
        }
    }
   
    return cnt;
}