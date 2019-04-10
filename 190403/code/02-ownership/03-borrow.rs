fn main() {
    let mut s = String::from("x");
    s.push('a');

    {
        let s2: &String = &s;
        let s3 = &s2;
        let s4 = &s;
        //let mut s5 = &mut s;
        
        println!("{} {} {} {}", s, s2, s3, s4);
        //s.push('a');
    }
    s.push('a');
}
