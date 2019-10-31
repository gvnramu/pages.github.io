import smtplib
from email.mime.text import MIMEText

content = None
with open("./sample.html", 'r') as f:
	content = f.read()
template = MIMEText(content, 'html')
# msg.attach(template)

gmail_user = 'gvnramu@gmail.com'
gmail_password = 'google@gvnr'

sent_from = gmail_user
to = ['gvnramu@gmail.com']
subject = 'OMG Super Important Message'
body = template

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except Exception as e:
    print (f'Something went wrong... {e}' )


# import requests
# def send_simple_message():
#     response = requests.post(
#         "https://api.mailgun.net/v3/sandboxaaf2949351ac4ca88ef2c136c294b29b.mailgun.org/messages",
#         auth=("api", "02cd782ca38cc39a72ee91b30aba88f7-2dfb0afe-b9980b3b"),
#         data={"from": ["bobby@sandboxaaf2949351ac4ca88ef2c136c294b29b.mailgun.org"],
#               "to": ["gvnramu@gmail.com"],
#               "subject": "Hello",
#               "text": "Sample Template"}
#               )
#     print(response.text)


# content = None
# with open("./sample.html", 'r') as f:
# 	content = f.read()
	
# # requests.post("https://api.mailgiun.net/v3/sandboxaaf2949351ac4ca88ef2c136c294b29b.mailgun.org/templates/sample/versions",
# #                        auth=("api","02cd782ca38cc39a72ee91b30aba88f7-2dfb0afe-b9980b3b"),
# #                        data={"tag": "v0",
# #                                  "comment": "version comment",
# #                                  "template": content})

# send_simple_message()