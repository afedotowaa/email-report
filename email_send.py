import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import time



def send_email(from_addr, to_addr_list,
              subject, plain_text_body,
              login,
              password,
              smtpserver='smtp.gmail.com:587',
              cc_addr_list=None,
              attachment=None,
              from_name=None):

    message=MIMEMultipart()

    plain=MIMEText(plain_text_body,'plain')

    message.add_header('from',from_name)
    message.add_header('to',','.join(to_addr_list))
    message.add_header('subject',subject)
    message.attach(plain)


    attach_file=MIMEApplication(open(attachment,"rb").read())
        # Add header to variable with attachment file
    # Add header to variable with attachment file
    attach_file.add_header('Content-Disposition', 'attachment', filename=attachment)
    # Then attach to message attachment file
    message.attach(attach_file)
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, to_addr_list, message.as_string())
    server.quit()
    print('mail sent at', datetime.now())



if __name__ == "__main__":
    start_time = time.time()
    while True:

        time.sleep(86400.0 - ((time.time() - start_time) % 86400.0))
        send_email(
                   from_addr='afedotowaaa@gmail.com',
                   to_addr_list=['a.fedotova@effema.com'],
                   subject=f'Отчет за {datetime.day}',
                   plain_text_body='Коллеги, доброго дня. Высылаю файлик по вложении, просьба ознакомиться',
                   login='afedotowaaa',
                   password='********',
                   from_name='Anastasia Fedotova',
                   attachment='report.pdf'
                   )