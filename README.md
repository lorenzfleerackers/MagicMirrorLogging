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
<p>Save the file end leave</p>

<h3>Install <a href="https://www.npmjs.com/package/express-logging">express-logging</a> to log the HTTP requests</h3>
<p>If you want to log the http requests that you made or those from <a href="https://github.com/Jopyth/MMM-Remote-Control.git">MMM-Remote-Control</a> or <a href="">MMM-ChangeConfig</a>
<ol>
  <li>Go to the module you want to log (this can be your own module or the one from above)</li>
  <li>Install the package with 
   <ul>
     <li>npm install express-logging</li>
     <li>npm install logops</li>
    </ul>
  </li>
  <li>Open the node_helper or the javascript file where you define your API's with express</li>
  <li>add the folowing code
  <pre>
    var express = require('express'),
        expressLogging = require('express-logging'),
        logger = require('logops');
    var app = express();
        app.use(expressLogging(logger));
  </pre>
  </li>
</ol>

<h2>What can you do with the logging?</h2>
<p>You can start the Magic Mirror with only showing the info/logs/error or the HTTP requests.</p>

<h3>npm run start:log</h3>
<table>
  <tr>
    <th>options</th>
    <th>explanation</th>
  </tr>
  <tr>
    <td>Start mirror without options</td>
    <td>Start the mirror and show all the logs,errors and requests</td>
  </tr>
  <tr>
    <td>Show info</td>
    <td>With this option the mirror will start and you will see console.info logs from all the modules without showing other errors or logs</td>
  </tr>
  <tr>
    <td>Show logs</td>
    <td>>With this option the mirror will start and you will seee console.log logs from all the modules without showing other errors or info</td>
  </tr>
  <tr>
    <td>Show errors</td>
    <td>With this option the mirror will start and show only the errors without all the logs or info</td>
  </tr>
  <tr>
    <td>Show requests</td>
    <td>With this option you will start the magic mirror without showing any logs or errors only the http requests from express-logging will be visible</td>
  </tr>
  <tr>
    <td>Leave</td>
    <td>Quit the option list without starting the mirror</td>
  </tr>
</table>
<h3>npm run start:searchLog</h3>
<table>
  <tr>
    <th>options</th>
    <th>explanation</th>
  </tr>
  <tr>
    <td>Show info</td>
    <td></td>
  </tr>
  <tr>
    <td>Show logs</td>
    <td</td>
  </tr>
  <tr>
    <td>Show errors</td>
    <td></td>
  </tr>
  <tr>
    <td>Show requests</td>
    <td></td>
  </tr>
  <tr>
    <td>Quit</td>
    <td></td>
  </tr>
</table>


