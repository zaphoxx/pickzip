# pickzip
Simple python based zipfile password cracker

# pickzip
# simple script to bruteforce a password protected zip/archive
# :usage pickzip.py -z <zipfile> -d <passwordlistfile> [-m <max threads>]
# optional is the --maxthreads argument where you can define a custom maximum thread number
# however the maximum possible thread number will be down adjusted dynamically if given value
# is to high and unsafe to use. default value is 15000 threads'
# 
# example: python3 pickzip.py -z mypwprotectedzip.zip -d rockyou.txt
#
# code is based on the 'Violent python' book but has been modified and adjusted to be in alignment with python3 syntax
