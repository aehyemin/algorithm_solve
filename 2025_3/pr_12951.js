function solution(s) {
    let array = s.split(" ")
    console.log(array)
    for(let i=0; i<array.length; i++) {
        array[i] = array[i].charAt(0).toUpperCase() + array[i].slice(1).toLowerCase();
    }
    return array.join(" ")

}