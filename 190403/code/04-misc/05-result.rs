fn main() {
    match "10e".parse::<i32>() {
        Ok(i) => println!("int={}", i),
        Err(s) => println!("err={}", s)
    }
}
