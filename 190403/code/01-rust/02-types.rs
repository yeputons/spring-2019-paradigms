fn main() {
    let a: i32 = 10;
    let b = 10;
    let c: u8 = 10;
    
    let d: isize = 20; // i32/i64
    let e: usize = 30; // u32/u64

    let f: u64 = c as u64;
    let g = 1000u128;
    
    let (v1, v2, v3) = (10, "x", 30);
    println!("v1={}, v2={}, v3={}", v1, v2, v3);
    
    let arr: [i32; 8] = [1, 2, 3, 4, 5, 6, 7, 8];
    println!("{:?}", arr);
    let arr = [1, 2, 3, 4, 5, 6, 7, 8];
    println!("{:?}", arr);
    let arr = ["x"; 3];
    println!("{:?}", arr);
}
