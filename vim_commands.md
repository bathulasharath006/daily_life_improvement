# VIM Commands

### Commands we are unaware

 - `dw` -> delete word
 - `d$` or `D` -> delete from cursor to till end of the line
 - `:r !command` -> read command output into vim editor
 - `gg` -> Go to First Line and First Character
 - `GA` -> Go to EOF & be in append mode ( `G` go to last line and `A` go to end of the line & be in append mode )

> **Fun Trick:** Add `:x` in `.vimrc` file in your friend's PC. From now on, whenever they open `vi` editor, they will be kicked out automatically.  


 - `%s/  \+/ /g` -> Squeeze multiple spaces with single space for the whole buffer.
 - `1,10left` or `1,10le` -> To format 1 to 10 lines to the *left*, `%` for whole buffer. Now you guess for right alignment!
 - `1,10right` or `1,10ri` -> To format 1 to 10 lines to the *right*, `%` for whole buffer.

- `:1,/pattern/-1d` -> Delete lines from 1 until the first occurrence of a pattern (Occurrence line is not deleted)
- `:,/pattern/d` -> Delete lines from current line to until the first occurrence of a pattern (Occurrence line is deleted)


