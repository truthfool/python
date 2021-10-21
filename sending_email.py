import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPException



def send_mail():
    #The mail addresses and password
    assigne_name="Ishan Ranasingh"
    sender_address = ''
    sender_pass = ''
    receiver_address = ''
    link=""
    
    mail_content = """From: %s<br>
    To: %s<br>
    Subject: OPENG2P Task<br>

    Your OPENG2P Task is pending.<br>
    Assigned by : <b>%s</b><br>

    Go to link : %s to complete your pending tasks.

    """%(sender_address,receiver_address,assigne_name,link)

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'OPENG2P Task'   

    
    message.attach(MIMEText(mail_content, 'html'))
    
    try:
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls() 
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        
        print("Email Sent")
    except SMTPException as e:
        print(e)


if __name__=="__main__":
    send_mail()