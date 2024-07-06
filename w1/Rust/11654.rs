use std::io::stdin;
fn main () {
    let mut input:String = String::new();
    stdin().read_line(&mut input).unwrap();
    let a = input.trim().as_bytes();
    println!("{}", a[0])
}