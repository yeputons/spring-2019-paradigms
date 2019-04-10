use std::thread;

fn main() {
    let t1 = thread::spawn(|| {
        println!("Hello");
    });
    let t2 = thread::spawn(|| {
        println!("World");
    });
    t1.join().unwrap();
    t2.join().unwrap();
}