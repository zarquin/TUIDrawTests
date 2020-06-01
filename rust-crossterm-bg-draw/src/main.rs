//TUIDrawTests
//Benchmarking for Terminal Drawing 
//zarquin@ucc.asn.au
//(c) 2020
//See LICENSE for licence details
//

use std::env;
//use crossterm::tty::IsTty;
use rand::Rng;

use std::io::{stdin, stdout, Write};

use crossterm::{QueueableCommand, cursor};

use crossterm::{
    queue,
    execute,
    style::{Color, Print, ResetColor, SetBackgroundColor, SetForegroundColor},
    ExecutableCommand, Result,
    event,
    tty::IsTty,
    terminal::{ScrollUp, SetSize, size, Clear, ClearType}
};

fn main() -> Result<()>  {
//fn main() {
    let mut rng = rand::thread_rng();
    let args: Vec<String> = env::args().collect();
    let count: i32 = args[1].parse().unwrap(); 
    println!("{:?}", args);
    println!("{}",count);
    if stdin().is_tty() {
        println!("Is TTY");
    } else {
        println!("Is not TTY");
    }
    let mut iini: u8 = rng.gen_range(0, 255);

    //let mut stdout = stdout();
    execute!(stdout(), Clear(ClearType::All))?;

    let (cols, rows) = size()?;

    //how many frames do we want to draw.
    for f in 0..count {
        for y in 0..rows {
            for x in 0..cols{
                //get a random colour.
                //move the cursor.
                //write the background.
                let iini = rng.gen_range(0, 255);
                queue!(stdout(), cursor::MoveTo(x,y), SetBackgroundColor(Color::AnsiValue(iini) ), Print(" ") )?;

            }
        }
        //update screen
        stdout().flush();
    }
    execute!(stdout(), ResetColor);
    Ok(())
}
