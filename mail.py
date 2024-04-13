import smtplib
import ssl
from email.message import EmailMessage


def mail_sender(name="user",email_receiver="",otp="",operation="",balance='',reciver_id=""):
    # Define email sender and receiver
    email_sender = 'your email'
    email_password = 'email password'
    subject = 'OTP'
    if operation == 'new':
        body = f"""
        Hello user, {otp} is your one time password to create your bank account \
            please don't share this otp with anyone.
        
        
        For any queries contact:-986575****
        """
    elif operation == "edit":
        body = f"""
        Hello {name}, {otp} is your one time password to change your account pin \
            please don't share this otp with anyone.
        
        
        For any queries contact:-986575****
        """

    elif operation == "credit":
        body = f"""
        Hello {name}, your transaction is completed successfully
        your current balance is ₹ {balance} \\-.
        
        
        For any queries contact:-986575****
        """

    elif operation == "debit":
        body = f"""
        Hello {name}, you recived money from {reciver_id}
        your current balance is ₹ {balance} \\-.
        
        
        For any queries contact:-986575****
        """

    elif operation == "invoice":
        body = f"""
        Hello {name}, your current balance is ₹ {balance} \\-.
        Your account id is {reciver_id}
        
        
        For any queries contact:-986575****
        """



    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


        
