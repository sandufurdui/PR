chat app with python

**fourth checkpoint:**<br />
-implemented smtp<br />
-added ftp_server.py<br />
-not client can send mails by using '!mail' command when chating<br />

**Get Started:**<br />
-run py server.py<br />
-run py client.py<br />

**Output:<br />
Client:**<br />
$ py client.py<br />
Username: alex<br />
alex > !mail<br />
What is you password: test321.<br />
Enter receiver email: sandu4561@gmail.com<br />
Enter the subject: Testing SMTP protocol<br />
Enter email body:This is a test lol<br />
successfully loged in<br />
now sending the mail<br />
mail successfully sent<br />
exiting...<br />
alex > <br />
<br />


**Server:**
Accepted new connection from 127.0.0.1:60982, username: test1<br />
Accepted new connection from 127.0.0.1:61015, username: test2<br />
Received message from test2: hi there<br />
Received message from test2: this is a message from test 2<br />
Received message from test1: and this one is from test 1<br />
Closed connection from: test1<br />
Closed connection from: test2<br />
