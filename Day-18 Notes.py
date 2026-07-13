""" SMTP Module
email.message
"""
import smtplib
import ssl
from email.message import EmailMessage
sender_email ="yogivarma2901@gmail.com"
password="rgxyvifhekhkkqmk"

receiver_email ="knsknsk10@gmail.com"
message = EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="Welcome Mail"
message.set_content(f"""Hello Yogesh!

Welcome to our python class

Regards,

Python Team

Modda Gudu ra   python sir dhi """)
context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)



