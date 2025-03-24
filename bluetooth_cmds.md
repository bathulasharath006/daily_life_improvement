`scan on`  
`remove XX:XX:XX:XX:XX:XX` # if it had already been paired  
`trust XX:XX:XX:XX:XX:XX`  
`pair XX:XX:XX:XX:XX:XX`  
`connect XX:XX:XX:XX:XX:XX`  
  
If you want to connect multiple devices simultaneously, enable multi-connect mode:  
`sudo vi /etc/bluetooth/main.conf`  
  
Enable: `MultiProfile = multiple`  
Restart Bluetooth: `sudo systemctl restart bluetooth`  
  
  
