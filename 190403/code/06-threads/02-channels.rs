use std::thread;
use std::sync::mpsc::{channel, Sender, Receiver};

fn main() {
    let (tx, rx): (Sender<i32>, Receiver<i32>) = channel();

    let tx1 = tx.clone();
    let t1 = thread::spawn(move || {
        println!("Hello");
        for i in 0..10000 {
            tx1.send(i).unwrap();
        }
    });

    let tx2 = tx.clone();
    let t2 = thread::spawn(move || {
        println!("World");
        for i in 10000..20000 {
            tx2.send(i).unwrap();
        }
    });

    tx.send(-100).unwrap();
    for _ in 0..=20000 {
        let result: i32 = rx.recv().unwrap();
        println!("{}", result);
    }
    t1.join().unwrap();
    t2.join().unwrap();
}