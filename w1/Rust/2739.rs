use std::io::stdin;


fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    let mut input = input.split_ascii_whitespace().flat_map(str::parse::<i32>);
    let N:i32 = input.next().unwrap();

    for i in 1..10 {
        println!("{} * {} = {}", N, i, N*i)
    }

}