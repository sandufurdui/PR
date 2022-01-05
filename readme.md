chat app with python

**third checkpoint:**<br />
-implemented ftp<br />
-added ftp_server.py<br />
-now the server supports multiple client connections<br />

**Get Started:**<br />
-run py server.py<br />
-run py client.py<br />

**Output:<br />
Client:**<br />
$ py client.py<br />
Choose an username: test2<br />
test2 > hi there<br />
test2 > this is a message from test 2<br />
test1 > and this one is from test 1<br />
<br />
$ py client.py<br />
Choose an username: test1<br />
test1 ><br />
alex > fad<br />
test2 > hi there<br />
test2 > this is a message from test 2<br />
test1 > and this one is from test 1<br />
test1 ><br />

**Server:**
Accepted new connection from 127.0.0.1:60982, username: test1<br />
Accepted new connection from 127.0.0.1:61015, username: test2<br />
Received message from test2: hi there<br />
Received message from test2: this is a message from test 2<br />
Received message from test1: and this one is from test 1<br />
Closed connection from: test1<br />
Closed connection from: test2<br />
