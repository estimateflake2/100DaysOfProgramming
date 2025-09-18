from smtplib import *
from dotenv import load_dotenv
import os

# When using gmail account you must first enable App Password:
#     Enable 2 step verification :
#     - Go to: myaccount.google.com → Security → 2-Step Verification
#     - Enter Password
#     - Turn on 2 Step Verification
#
#     Get App Password:
#     - go to: https://myaccount.google.com/apppasswords
#     - If blocked, try these steps, Go back to Security > How you sign in to Google.
#     - Turn off “Skip password when possible.”
#     - If it still doesn’t show: Confirm you’re using a personal Gmail account, not a Workspace account.
#   NOTE: gmail does not allow port 25 for SMTP, switch to port 587

#loading .env
load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_password=os.getenv("MY_PASSWORD")
to_email = 'oladipo.bankole@gmail.com'

print ('my_email:  ',my_email)
print ('my_password:  ',my_password)

with SMTP("smtp.gmail.com", 587, timeout=30) as connection: #smtp(sender's hostmail,
    connection.starttls()
    connection.login(user= my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg= 'Subject:Hello World\n\nTHis is the body of my email'
                        )
