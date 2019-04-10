fn main() {
    let mut x = String::from("hello");
    {
        let mut f = || x.push('a');
        f();
        f();
        // println!("{}", x);
    }
    println!("{}", x);
}
