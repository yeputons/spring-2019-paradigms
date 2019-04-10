fn main() {
    let mut v = Vec::new();
    v.push(1);
    println!("{:?}", v);

    let v2 = vec![1, 2, 3];
    let v2 = {
        let mut v = Vec::new();
        v.push(1);
        v.push(2);
        v.push(3);
        v
    };
}
