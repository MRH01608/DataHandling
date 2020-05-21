import re, os
from subprocess import call

path = "/run/user/1000/gvfs/smb-share:server=goodwin-ufmf,share=dlc_temp/MH_DLC_CutVids/W4"
file = open('FPS_Overlays.sh','w')
	
for i in os.listdir(path):
	if i.endswith(".mp4"):
		string = '\"'+str(i)+'\"'
		fileOut = string[0:17]
		# print(string)
		# print(fileOut)
		call(["echo", "ffmpeg -i", string, "-vf \"drawtext=fontfile=Arial.ttf: text='%{frame_num}': start_number=1: x=(w-tw)/2: y=h-(2*lh): fontcolor=black: fontsize=20: box=1: boxcolor=white: boxborderw=5\" -c:a copy", fileOut+'_FRAMES.mp4\"\n'], stdout=file)
file.close()