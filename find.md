# find

[More info on `find` from web](https://www.baeldung.com/linux/find-command)

`find /home/user -type f -name "*.jpg" `  # find path -type d,f -name "*word*"

`find . -iregex ".*\.jpg$"`  # Case insensitivity search using regex

```
type :- To search for more than one type at once, you can supply the combined list of type letters separated by a comma `,' (GNU extension).

 b- block (buffered) special
 c- character (unbuffered) special
 d- directory
 p- named pipe (FIFO)
 f- regular file
 l- symbolic link; 
 s- socket
 D- door (Solaris)
```


