use std::fmt;

#[derive(Debug)]
struct Point {
   x: i32,
   y: i32
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

fn main() {
    let p = Point { x: 10, y: 10 };
    println!("{}", p);
}
