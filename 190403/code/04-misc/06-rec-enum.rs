enum List<T> {
    Empty,
    NonEmpty(T, Box<List<T>>)
}

fn main() {}
