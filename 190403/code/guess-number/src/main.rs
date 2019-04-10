extern crate rand;

use std::io::stdin;
use rand::thread_rng;
use rand::Rng;

fn main() {
    let number = thread_rng().gen_range(1, 101);
    println!("Guess a number between 1 and 100");
    loop {
        println!("Your guess:");
        let mut guess = String::new();
        stdin().read_line(&mut guess).expect("Unable to read line");
        let guess: i32 = guess.trim().parse().expect("Not a number");

        if guess < number {
            println!("Too small");
        } else if guess > number {
            println!("Too big");
        } else {
            println!("Correct!");
            break;
        }
    }
}
