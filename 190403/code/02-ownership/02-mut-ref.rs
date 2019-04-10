fn my_push(s: &mut String) {
    s.push(',');
}

fn my_push_2(mut s: String) -> String {
    s.push(',');
    s
}

fn my_inc(x: &mut i32) {
    *x += 1;
}

fn main() {
    let mut s = String::from("hello");
    my_push(&mut s);
    s = my_push_2(s);
    println!("{}", s);

    let mut i = 10;
    my_inc(&mut i);
    assert_eq!(i, 11);
}
