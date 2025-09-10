
- Refresh All Snap Packages
  - `sudo snap refresh`

- Refresh a Specific Snap Package
  - sudo snap refresh firefox`

- Check for Available Updates Without Installing
  - snap list

- Automatically Refreshing
  - Check the current refresh schedule:
    - `snap refresh --time`
  - This will make Snap only check for updates between 2 AM and 4 AM.
    - `sudo snap set system refresh.timer=02:00-04:00`
