'''
#	Python OSINT Tool
	Enter a phone number or email address as an argument
	IF API allows
		grab data from sources
	Output data into a folder

'''
import	sys						#modules used

spokeo_apikey 	=""
google_apikey 	=""
bing_apikey   	="" 
targetnum = sys.argv[1]

usage = "python-osint.py <phone number>"

def banner():

def googleimage(targetnum):

def bingimage(targetnum):

def main():
	if sys.argv == 2:
		banner()
		googleimage(targetnum)
		bingimage(targetnum)

if __name__ = "__main__":
	main()
