## Sticky Bit  
  - It is a special type of file permission in unix-like systems, only applied on directories.
  - At the end of permission string, `t` represents sticky bit is On.  
  - To set sticky bit: `chmod +t directory` or **1** in front of octal permission number.
    - Ex:- `chmod 1755 directory`  
  - Typically, found on `/tmp` directory.  
  - It allows only root, directory owner, file owner to delete or rename the file(s).  


## Interesting Commands
  - `mc` - **M**idnight **C**ommander, a character-based directory browser and file manager.  

