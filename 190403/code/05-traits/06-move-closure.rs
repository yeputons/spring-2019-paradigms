fn make_print(text: String) -> impl Fn() -> () {
    return move || {
        println!("{}", text);
    };
}

fn main() {
    let f = make_print("hello".to_string());
    f();
    f();
    f();
}
