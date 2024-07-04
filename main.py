import smtplib
import ssl
import maskpass

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "khurana.luv30@gmail.com"
receiver_email = "sahni.anchal@gmail.com"
password = maskpass.askpass(prompt="Password:", mask="#")
message = """\
Subject: Hi there
This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login('khurana.luv30@gmail.com', password)
    server.sendmail("khurana.luv30@gmail.com", 'sahni.anchal@gmail.com', message)