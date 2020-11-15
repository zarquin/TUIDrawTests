use std::cmp::{max, min};
use tuikit::prelude::*;
use std::time::Duration;
use std::env;
use tuikit::attr::{Attr, Color};
//use rand::Rng;

fn main() {
    //let term: Term<()> = Term::with_height(TermHeight::Percent(30)).unwrap();
    let args: Vec<String> = env::args().collect();
    let count: i32 = args[1].parse().unwrap(); 

    let term = Term::<()>::new().unwrap();
    let mut row = 1;
    let mut col = 0;

    let _ = term.print(0, 0, "press arrow key to move the text, (q) to quit");
    let _ = term.present();

    let mut jug: u8 = 0;
    jug = 0;

    //while let Ok(ev) = term.poll_event() {
    let _ = term.clear();
    //let _ = term.print(0, 0, "press arrow key to move the text, (q) to quit");

    let (width, height) = term.term_size().unwrap();

    for n in 0..count  {

        let attr = Attr { bg: Color::AnsiValue(jug), effect: Effect::BOLD, ..Attr::default() };

        for xx in 0..height {
            for yy in 0..width {
                let attr = Attr { bg: Color::AnsiValue(jug), effect: Effect::BOLD, ..Attr::default() };
                let _ = term.print_with_attr(xx,yy," ", attr);
                jug +=1;
                if jug >= 255{
                    jug = 0;
                }
            }
        }
        //let _ = term.print_with_attr(row, col, &format!("col: {} row:{}",col, row), Color::RED);

        //let _ = term.print_with_attr(row+1, col+1, &format!("{:?}",ev), attr );
        //let _ = term.set_cursor(row, col);
        let _ = term.present();

        jug +=1;
        if jug >= 255{
            jug = 0;
        }
    }
}
