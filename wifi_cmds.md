You can manage WiFi connections in Linux from the command line using `nmcli` (Network Manager CLI) or `iwctl` (for systems using iwd).  

---

## **1. Check Available WiFi Networks**  
To list available networks:  
```bash
nmcli device wifi list
```

For real-time scanning:
```bash
watch -n 2 nmcli device wifi list
```

If `nmcli` is not installed, you can use `iwlist` (older method):
```bash
sudo iwlist wlan0 scan | grep 'ESSID'
```

---

## **2. Connect to a WiFi Network**  
### **Method 1: Using `nmcli` (Recommended)**
```bash
nmcli device wifi connect "SSID_NAME" password "WiFi_PASSWORD"
```

---

### **ESSID vs. SSID vs. BSSID**
| Term | Full Form | Meaning | Example |
|------|-----------|---------|---------|
| **SSID** | Service Set Identifier | Name of a WiFi network | `MyHomeWiFi` |
| **ESSID** | Extended Service Set Identifier | Same as SSID (used in extended networks) | `MyHomeWiFi` |
| **BSSID** | Basic Service Set Identifier | MAC address of an individual access point | `AA:BB:CC:11:22:33` |

---
For hidden networks:
```bash
nmcli device wifi connect "SSID_NAME" password "WiFi_PASSWORD" hidden yes
```

### **Method 2: Using `wpa_supplicant` (For Minimal Setups)**
1. Create a WPA configuration file:
```bash
wpa_passphrase "SSID_NAME" "WiFi_PASSWORD" | sudo tee /etc/wpa_supplicant.conf
```
2. Connect:
```bash
sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
```
3. Get an IP address:
```bash
sudo dhclient wlan0
```

---

## **3. Disconnect from WiFi**
To disconnect from the current network:
```bash
nmcli device disconnect wlan0
```

To disable WiFi completely:
```bash
nmcli radio wifi off
```

To enable WiFi again:
```bash
nmcli radio wifi on
```

---

## **4. List Saved WiFi Connections**  
To see all saved networks:
```bash
nmcli connection show
```

To delete a saved WiFi connection:
```bash
nmcli connection delete "SSID_NAME"
```

---

## **5. Switch Between WiFi Networks**  
To switch to a different WiFi network:
```bash
nmcli connection up "NEW_SSID"
```

If auto-connect is causing issues:
```bash
nmcli connection modify "SSID_NAME" connection.autoconnect no
```

---

## **6. Check WiFi Status and IP Address**
To check current connection details:
```bash
nmcli device show wlan0
```

To check the IP address:
```bash
ip a show wlan0
```

---

## **7. Troubleshooting WiFi Issues**
- Restart the network manager:
  ```bash
  sudo systemctl restart NetworkManager
  ```
- Check logs for errors:
  ```bash
  journalctl -u NetworkManager --no-pager | tail -n 50
  ```
- Reset WiFi adapter:
  ```bash
  sudo ip link set wlan0 down && sudo ip link set wlan0 up
  ```
- Reboot:
  ```bash
  sudo reboot
  ```

Let me know if you need further customization! 🚀
