from pywinauto import application
import time
import os
from secretCon import get_secret

pwf=get_secret('PW')
pwc=get_secret('PW_CERT')

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:wang9 /pwd:'+pwf+'/pwdcert:'+pwc+'/autostart')
time.sleep(60)