
/* 
문제
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
시험 성적을 출력한다.

예제 입력 1 
100
예제 출력 1 
A
*/


// use std::io::stdin;

// fn main() {
//     let mut input = String::new();
//     stdin().read_line(&mut input).unwrap();
//     let mut input = input.split_ascii_whitespace().flat_map(str::parse::<i32>);
//     let a:i32 = input.next().unwrap();
  
//     if a >= 90 {
//         println!("A");
//     } else if a >= 80 {
//         println!("B");
//     } else if a >= 70 {
//         println!("C");
//     } else if a >= 60 {
//         println!("D");
//     } else {
//         println!("F")
//     }
// }

use std::io::stdin;

fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    let mut input = input.split_ascii_whitespace().flat_map(str::parse::<i32>);
    let a:i32 = input.next().unwrap();
  
    let result = if a >= 90 {
        "A"
    } else if a >= 80 {
        "B"
    } else if a >= 70 {
        "C"
    } else if a >= 60 {
        "D"
    } else {
        "F"
    };
    println!("{}", result);
}
