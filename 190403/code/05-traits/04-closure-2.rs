fn main() {
    let mut x = String::from("hello");
    let mut f = || {
       x.push('a');
       x
    };
    f();
    println!("{}", f());
}
