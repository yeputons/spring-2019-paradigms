/*enum Option<T> {
    Some(T),
    None
}*/

fn parse_digit(s: &str) -> Option<i32> {
    if s.len() != 1 {
        return None;
    }
    let c = s.chars().next().unwrap();
    if '0' <= c && c <= '9' {
        Some(c as i32 - '0' as i32)
    } else {
        None
    }
}

fn main() {
    println!("{:?}", parse_digit("xxx"));
    println!("{:?}", parse_digit("x"));
    println!("{:?}", parse_digit("3"));
    match parse_digit("4") {
        Some(1) => println!("wtf"),
//        Some(x) => println!("hurray {}", x),
//        None => println!("wtf??")
        _ => println!("wtf")
    }

    let z = match parse_digit("1") {
        Some(x) => x,
        None => {
            println!("oops");
            0
        }
    };
    println!("z={}", z);

    match parse_digit("1") {
        Some(x) => {
            println!("hurray {}", x);
        },
        None => {}
    }

    if let Some(x) = parse_digit("1") {
        println!("hurray {}", x);
    }
}
