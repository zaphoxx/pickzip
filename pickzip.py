#!/usr/bin/python3
# pickzip
# simple script to bruteforce a password protected zip/archive
# :usage pickzip.py -z <zipfile> -d <passwordlistfile>
# optional is the --maxthreads argument where you can define a custom maximum thread number
# however the maximum possible thread number will be down adjusted dynamically if given value
# is to high and unsafe to use. default value is 15000 threads'

# title: pickzip
# file: pickzip.py
# author: zaphoxx
# checkout: https://github.com/zaphoxx/
# latest update: 12/16/2016 

import argparse
import zipfile
import threading

class cThread (threading.Thread):
	def __init__(self,threadID,name,zip,pw):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.zip=zip
		self.pw=pw
	def run(self):
		# print("[+] starting {}".format(self.name))
		processZipFile(self.zip,self.pw)

def processZipFile(zipFile,password):
	global exitFlag
	try:
        # currently using 'latin-1' you might want to modify
        # this to your needs
		zipFile.extractall(pwd=bytes(password,"latin-1"))
		print("[+] Found password: '{}'".format(password))
		exitFlag=True
	except:
		pass

def initParser(parser):
	try:
		parser.add_argument("-z","--zipfile",dest="zipFilename",required=True,help="Provide filename of password protected zipfile.")
		parser.add_argument("-p","--passfile",dest="pwFilename",required=True,help="Provide filename of password dictionary.")
		parser.add_argument("-m","--maxthreads",dest="maxThreadCount",type=int,required=False,default=15000,help="Define the maximum number of threads to be started.")
		args=parser.parse_args()
		# parser.print_help()
		return args
	except:
		parser.print_help()
		exit(0)

def handleThread(hThread,maxThreads):
	# handleThread will test if the tread can be started
	# a fail will adjust the maximum number of threads maxThreadCount
	# and recall handleThread with the adjusted value
	# this will repeat until the thread can be safely started
	
	# dont exceed the max number of threads
	while(threading.activeCount()>maxThreads):
		pass
	try:
		hThread.start()
	except:
		# adjust maximum number of threads down by hundreds
		maxThreads=maxThreads - 100
		# print("[+] maxThreadCount={}".format(maxThreads))
		# make sure the active threadcount is below maximum thread
		# prior starting a new thread
		while(threading.activeCount()>maxThreads):
			pass
		# hThread.start() by calling handleThread()
		maxThreads=handleThread(hThread,maxThreads)
	
	# feedback adjusted maximum number of threads
	return maxThreads
	
def main():
	# default values

	# brief title
	parser=argparse.ArgumentParser(description="pickzip / simple zipfile password cr4cker")
	# parse commandline arguments
	args=initParser(parser)
	#print(parser.usage())
	if (args.zipFilename==None or args.pwFilename==None):
		parser.print_help()
		exit(0)
	# print parsed arguments for reference
	print("[+] target zipfile: '{}'".format(args.zipFilename))
	print("[+] password dictionary: '{}'".format(args.pwFilename))
	
	# open zipfile for processing
	zFile=zipfile.ZipFile(args.zipFilename)

	# open dict file for password looping
	pwFile=open(args.pwFilename,"r",encoding="utf=8",errors="replace")
	i=0
	maxThreadCount=args.maxThreadCount
	for word in pwFile.readlines():
		password=word.strip('\n')
		#print("[+] {}".format(password))
		if not exitFlag:
			# do not create additional threads if max thread limit has been reached.
			if(i%10000==0):
				print("[+] thread-id <{}>".format(i))
			
			newThread=cThread(i,"t-{}".format(i),zFile,password)
			maxThreadCount=handleThread(newThread,maxThreadCount)
			i+=1
		
				
		else:
			newThread.join()
			break
	
	# close files
	pwFile.close()
	
if __name__=="__main__":
	exitFlag=False
	main()
