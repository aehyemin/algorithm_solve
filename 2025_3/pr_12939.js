function solution(s) {
    let array = s.split(" ")

    array = array.map(Number)
    
    let min = Math.min(...array)
    let max = Math.max(...array)

    return `${min} ${max}`;
    
}