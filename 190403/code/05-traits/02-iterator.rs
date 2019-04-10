fn main() {
    let v = vec![10, 21, 30];
    for x in v.iter()
             .filter(|x| (*x) % 2 == 0)
             .map(|x| x * x)
    {
        println!("{}", x);
    }
}
