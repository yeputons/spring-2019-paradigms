fn sum(n: i32) -> i32 {
    let mut s = 0;
    for i in 0..n {
        s += i;
    }
    s
}

fn main() {
    println!("{}", sum(10));
}
