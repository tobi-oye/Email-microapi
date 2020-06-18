import smtplib

"""This function sends an email notification to the user when they login"""

def login_notification():
    user_email = 'you@email.com'
    user_password = 'P@ssword!'
    sent_from = user_email
    to = ['foo@gmail.com', 'bar@gmail.com']       
    subject = 'Login Notification'
    body = 'Your Account {} was logged in, if this was you please ignore this otherwise contact support'.format(user_email)

    email_text = """\
    From: {}
    To: {}
    Subject: {}

    {}

    """.format(sent_from, ", ".join(to), subject, body)


    try:
        server = smtplib.SMTP_SSL('smtp.sendgrid.net', 587)
        server.ehlo()
        server.login(user_email, user_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
login_notification()
