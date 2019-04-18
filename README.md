# Magic Mirror Logging
<h2>This is for logging the Magic Mirror on your Raspberry Pi</h2>

<h3>First you need to install the Magic Mirror</h3>
<a href="https://github.com/MichMich/MagicMirror">Magic Mirror</a>

<h3>After that you need to install the "MMM-Logging" module on your Magic-Mirror.</h3>
<a href="https://github.com/shbatm/MMM-Logging">MMM-Logging</a>

<h3>As last you need to clone this repo in the Raspberry Pi home directory</h3>
<pre>
cd ~
git clone https://github.com/lorenzfleerackers/MagicMirrorLogging.git
</pre>
<p>When you cloned the repo copy the logging.py file to the MagicMirror directory.</p>
<pre>cp ~/MagicMirrorLogging/logging.py ~/MagicMirror</pre>

<h3>Use npm scripts to start the logging</h3>
<pre>
cd ~/MagicMirror
nano package.json
</pre>
<p>Add the following lines
<pre>
"start:log": "python logging.py",
"start:searchLog": "python /home/pi/MagicMirrorLogging/localLogging.py",
</pre>
</p>
<p>after : <pre>"start": "sh run-start.sh",</pre></p>



