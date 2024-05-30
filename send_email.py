import smtplib
import ssl, os
import temp

temp.init()
def sendemail(message, receiver):
    host = 'smtp.gmail.com'
    port = 465

    username = 'bigalsworth@gmail.com'
    password = temp.vars['password']


    context = ssl.create_default_context()




    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
