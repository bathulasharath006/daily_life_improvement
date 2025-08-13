### Common mistakes which we tend to do in bash scripting

Exit code is 1 of `(( ))` syntax when the value evaluates to zero.  
For any none zero value, exit code is 0 (Success) 

Example:

```bash
>> (( 0 ))
>> echo $?
1 # Failure

>> (( -10 ))
>> echo $?
0 # Success
```

