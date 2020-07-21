import smtplib
import traceback
import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dateutil.relativedelta import relativedelta
from string import Template
import socket


socket.getaddrinfo('localhost', 8080)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_ID = "" #Sender Email ID here
SENDER_PASS = "" #Sender Password


# Function to send mail to our customers once they register!

def Send_Email_On_Register(Udata):
    RECEIVER_ID = Udata["email"]

    for emailID in RECEIVER_ID:
        try:
            print('Sending email to ... {}'.format(emailID))
            FROM = SENDER_ID
            TO = emailID
            html = """<html>
              <head>
              </head>
              <body>
              <p>
                  <br>
                  Hi <b>$username</b>,  
                  <br>
                  Thank you for signing up with us. 
                  <br>
                  Your credentials to log in are:
                  <br>
                  <b>Username:</b> $username
                  <br>
                  <b>Password:</b> $password
                  <br>
                  You can download the report from the link: $downLink
                  <br/>You can also visit our website for more information : <a href="https://www.google.co.in/"> 
                  <b>Healthy Life at BMSCE</b> </a>                 
                  <br><br><br>
                  <i>Regards, <br>
                  VDHRM Team.</i>
              </p>              
              </body>
            </html>
            """
            s=Template(html).safe_substitute(username=Udata["Name"],password="13246",downLink=Udata["DownloadLink"])
                     
            msg = MIMEMultipart('alternative')

            msg["Subject"] = "Healthy Life from BMSCE!"
            msg["Message-id"] = email.utils.make_msgid()
            msg["From"] = FROM
            msg["To"] = TO

            host = SMTP_SERVER
            server = smtplib.SMTP(host, SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.login(SENDER_ID, SENDER_PASS)
            part1 = MIMEText(s, 'html')
            msg.attach(part1)
            server.sendmail(FROM, TO, msg.as_string())
            server.quit()
            print("Email Sent!")
            return True
        except Exception as e:
            print(e)
            traceback.print_exc()
            return False


# Function to send mail to our customers once they go for a test!

def Send_Email_On_Test(Udata):
    emailID = Udata['email']
    RECEIVER_ID = Udata["email"]

    for emailID in RECEIVER_ID:
        try:
            print('Sending email to ... {}'.format(emailID))
            FROM = SENDER_ID
            TO = emailID
            html = """<html>
              <head>
              </head>
              <body>
              <p>
                  <br>
                  
                  Hi <b>$username</b>,                    
                  <br>
                  Your report from the test you took is attached below:                   
                  <br>
                  <a href=$downLink>Click here to download the report</a><br>
                    <br/><a href=$downLink>Click here to download our Android App</a> to explore more options.:)<br>

                  <br>               
                  You can also visit our website for more information : <a href="https://www.google.co.in/"> 
                  <b>Healthy Life at BMSCE</b> </a>                 
                  
                  <br>
                  
                  <i>Regards, <br>
                  VDHRM Team.</i>
              </p>              
              </body>
            </html>
            """
            s=Template(html).safe_substitute(username=Udata["Name"],downLink=Udata["DownloadLink"])

            msg = MIMEMultipart('alternative')

            msg["Subject"] = "Test report from VDHRM!"
            msg["Message-id"] = email.utils.make_msgid()
            msg["From"] = FROM
            msg["To"] = TO

            host = SMTP_SERVER
            server = smtplib.SMTP(host, SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.login(SENDER_ID, SENDER_PASS)
            part1 = MIMEText(s, 'html')
            msg.attach(part1)
            server.sendmail(FROM, TO, msg.as_string())
            server.quit()
            print("Email Sent Successfully!")
        except Exception as e:
            print(e)
            traceback.print_exc()

