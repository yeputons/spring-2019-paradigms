fn main() {
    let mut arr = [1, 2, 3, 4];
    
    let subarr = &mut arr[1..3];
    //let subarr2 = &mut arr[0];
    println!("{:?}", subarr);
    //println!("{:?}", subarr2);

    let mut s = String::from("hello world");
    let (hello, world): (&mut str, &mut str) = s.split_at_mut(6);
    println!("|{}|{}|", hello, world);
}