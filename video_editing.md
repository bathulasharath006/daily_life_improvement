----------------------------
| How to Cut a Video File? |
----------------------------

Step:1 ==> sudo ln -s /usr/bin/ffmpeg /usr/bin/avconv

Step:2a ==> avconv -i SourceFileName.mkv -c:a copy -c:v copy -ss hh:mm:ss.xxx -t hh:mm:ss.xxx OutputFileName.mkv

# -ss Start time: hh:mm:ss.xxx here .xxx milli seconds Optional AND
# -t is duration (not end time), duration may be either in seconds [600] or in "hh:mm:ss.xxx" form.


Step:2b ==> avconv -i SourceFileName.mkv -c:a copy -c:v copy -ss hh:mm:ss.xxx -to hh:mm:ss.xxx OutputFileName.mkv

# -ss Start time: hh:mm:ss.xxx here .xxx milli seconds Optional AND
# -to End time[upto] : hh:mm:ss.xxx here .xxx milli seconds Optional

#==================================================================================================#

--------------------------------------
| How to Merge Multiple Video Files? |
--------------------------------------

Step:1 ==> sudo apt install mkvtoolnix

Step:2 ==> mkvmerge -o OutPut_FileName.mkv Input_1.mkv + Input_2.mkv + Input_3.mkv + Input_4.mkv 

#==================================================================================================#

