fn main() {
     println!("{}",
         if 2 * 2 == 4 {
             println!("Hello!");
             "yes"
         } else { "wtf "}
     );

     {
         let mut i = 0;
         while i < 4 {
             println!("{}", i);
             i += 1;
         }
     }

     let x = {
         let mut i = 0;
         loop {
             i += 1;
             if i == 3 {
                 break i;
             }
         }
     };
     assert_eq!(x, 3);

     let mut y = 0;
     loop {
         y += 1;
         if y == 3 {
             break;
         }
     }
     let y = y;
     assert_eq!(y, 3);
     
     {
        let arr = [1, 2, 3, 4];
        for (i, x) in arr.iter().rev().enumerate() {
            println!("x[{}]={}", i, x);
        }
     }
}
