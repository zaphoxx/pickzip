<h1>pickzip</h1>
<h2>Simple python based zipfile password cracker</h2>

<h3>
simple script to bruteforce a password protected zip/archive
</h3>
<p>
<code>usage: pickzip.py -z zipfile -d passwordlistfile [-m maxthreads]</code></p>
use <code>pickzip.py --help</code> for list of options
<p>optional is the <code>--maxthreads</code> argument where you can define a custom maximum thread number
however the maximum possible thread number will be down adjusted dynamically if given value
is to high and unsafe to use. default value is 15000 threads'<p>
<p>Note: maxthreads is NOT dynamically upped yet. so any adjustments done are just to lower the maximum number of possible threads.</p>
<p><pre>
example: python3 pickzip.py -z mypwprotectedzip.zip -d rockyou.txt</pre></p>

<p>code is based on the 'Violent python' book but has been modified and adjusted to be in alignment with python3 syntax</p>

