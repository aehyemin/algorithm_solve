use std::io::stdin;

fn main() {
   
    let mut max_n = 0;
    let mut max_i = 0;

    for i in 0..9 {
        let mut a = String::new();
        stdin().read_line(&mut a).unwrap();
        // let mut input = input.split_ascii_whitespace().flat_map(str::parse::<i32>);
        let a:i32 = a.trim().parse().unwrap();

        if a > max_n {
            max_n = a;
            max_i = i + 1;
        }
 
    }
    println!("{}", max_n);
    println!("{}", max_i);
}