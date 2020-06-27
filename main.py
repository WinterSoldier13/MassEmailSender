import pandas as pd
from smtplib import SMTP
from tqdm import tqdm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


dataframe = pd.read_csv('/home/wintersoldier/Downloads/emails.csv')
dataframe.head()

names=[]
emails=[]
count = 0

for name in dataframe['Name']:
    names.append(name)
for email in dataframe['Email Address']:
    emails.append(email)
    count-=-1




print('High-Orbit-Email bombarder (MODIFIED) ~by WinterSoldier')
print('Please make sure that you have allowed less secure app access in your Google Account Settings')

print('\n\n')

email = 'someone@gmail.com'
password = 'PASSfuckingWord'



n = len(names)
print("Total messages to be sent: ",n)

try:
    mail = SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)
    for i in tqdm(range(n)):
    
    
#         print('Sending to :',names[i])
#         TEXT = 'Hi, '+names[i]
#         SUBJECT = "Hey, "+names[i]+" you've been invited."

      
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Hello, "+names[i]
        msg['From'] = 'Someone Anonymous'
        msg['To'] = emails[i]
        
        text = "Hi"
        html = """
        <html>
          <head></head>
          <body></body>
        </html>
        """


        
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        
        msg.attach(part1)
        msg.attach(part2)
        
        recv = emails[i]
        
        mail.sendmail(email, recv, msg.as_string())
        
        
    
        
        
#         message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        
#         recv = emails[i]
#         mail.sendmail(email,recv,message)
        
    mail.quit()
except:
    
    print("ERROR... check your mailID/password or make sure that you have enabled access to Google Account... for more plz contact the developer")

