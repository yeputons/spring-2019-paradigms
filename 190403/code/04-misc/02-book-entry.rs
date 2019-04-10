#[derive(Debug)]
struct BookEntry {
    name: String,
    phone: String
}

impl BookEntry {
    fn empty() -> BookEntry {
        BookEntry {
            name: String::new(),
            phone: String::new(),
        }
    }

    fn is_empty(&self) -> bool {
        self.name.len() == 0 && self.phone.len() == 0
    }
}

fn main() {
    let x;
    if 2 * 2 == 4 {
        x = BookEntry {
            name: String::from("Vasya"),
            phone: String::from("8 800")
        };
    } else {
        println!("hello");
        x = BookEntry {
            name: String::from("Vasya"),
            phone: String::from("8 800")
        };
    }

    let y = BookEntry::empty();
    println!("{}", y.is_empty());

    println!("{:?}", x);
}
