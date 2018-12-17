import glob
import os

print("""
Please make sure you have edited the script to set your "Logs" directory!
it is required for it to work!

How to use:
Join a Roblox game and wait until the game fully loads
Run this script while in the game
Press enter when you are ready to pull the IP!

P.S Please ignore the weird text before the IP, dunno how to remove it...

Please press ENTER to grab the IP...
""")
try:
    input("Press [ENTER] to grab the IP!")
except SyntaxError:
    pass
list_of_files = glob.glob('C:\Users\LeeEverett\AppData\Local\Roblox\logs\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
roblox_log = open(latest_file, 'r')

for line in roblox_log:
    if 'Connection accepted from' in line:
        line = line.replace('Connection accepted from', '')
        line2 = line.replace('|', ':')
        line3 = line2[23:]
        print("Server IP:" + line3)
