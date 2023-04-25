import smtplib
from email.mime.text import MIMEText
from email.header import Header
from data_pass_for_prod import gmail_pass, MAIL_FROM


def send_mail(message: str, subject: str, dest_email: str):
    email = MAIL_FROM  # ОТ КОГО
    password = gmail_pass
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = email
    msg['To'] = dest_email
    # server.set_debuglevel(1)  # Необязательно; так будут отображаться данные с сервера в консол__и
    server.sendmail(email, dest_email, msg.as_string())
    server.quit()
