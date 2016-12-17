<h1>pickzip</h1>
<h2>Simple python based zipfile password cracker</h2>

<h3>
simple script to bruteforce a password protected zip/archive
<it>usage: pickzip.py -z zipfile -d passwordlistfile [-m maxthreads]</it>
use pickzip.py --help for list of options
optional is the --maxthreads argument where you can define a custom maximum thread number
however the maximum possible thread number will be down adjusted dynamically if given value
is to high and unsafe to use. default value is 15000 threads'
</h3>

<p>example: python3 pickzip.py -z mypwprotectedzip.zip -d rockyou.txt</p>

<p>code is based on the 'Violent python' book but has been modified and adjusted to be in alignment with python3 syntax</p>
