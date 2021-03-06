import pandas as pd
from smtplib import SMTP
from tqdm import tqdm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




dataframe = pd.read_csv('/home/wintersoldier/Downloads/emails.csv')
print(dataframe.head())

names=[]
emails=[]
count = 0

for name in dataframe['Name']:
    names.append(name)
for email in dataframe['Email Address']:
    emails.append(email)
    count-=-1




print('High-Orbit-Email Canon ~by WinterSoldier')
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
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Hello, "+names[i]
        msg['From'] = 'Someone Anonymous'
        msg['To'] = emails[i]
        
        text = "Hi"
        html = """
        <html>
          <head></head>
          <body>
            <h1>Hello World</h1>
            <p>How you doin'</p>
          </body>
        </html>
        """


        
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        
        msg.attach(part1)
        msg.attach(part2)
        
        recv = emails[i]
        
        mail.sendmail(email, recv, msg.as_string())
        
    mail.quit()
except:
    
    print("ERROR... check your mailID/password or make sure that you have enabled access to Google Account... for more plz contact the developer")

