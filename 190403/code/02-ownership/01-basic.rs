fn foo(s: String) {}

fn print_text(s: &str) {
    println!("text: {}", s);
    foo(s.to_string());
}

fn main() {
    let mut s = String::from("hello");
    s.push(',');
    s.push_str(" мир!");

    print_text(&s);
    print_text(&s[1..]);

    println!("{} {}", s, s.len());

    let s2 = s;
    println!("{}", s2);

    // println!("{}", s);
}
