enum Something {
     Just(i32),
     None
}

fn main() {
    let x = Something::Just(10);
    let y = Something::None;
}
