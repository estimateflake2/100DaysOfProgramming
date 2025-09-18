from smtplib import *
from dotenv import load_dotenv
import os
import  random
from  datetime import datetime
from email.message import EmailMessage
import get_gmail_addresses as load_email
import csv
import datetime as dt

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
my_email = os.getenv("SEC_EMAIL")
my_password=os.getenv("SEC_PASSWORD")
quotes_list = []

#get content from quotes.txt
def get_quotes_file():
    global quotes_list
    with open("quotes.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if " - " in line:  # only process lines that follow the pattern
                quote, author = line.rsplit(" - ", 1)  # split only on last " - "
                quotes_list.append({
                    "quote": quote.strip('" '),  # remove extra quotes/spaces
                    "author": author.strip()
                })

#get Emmails from file
def read_emails_from_csv(path="gmail_addresses.csv"):
    emails = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            if row:  # skip empty lines
                emails.append(row[0].strip().lower())
    return emails


#Send Email Method
def send_email():
    msg = EmailMessage()
    msg["From"] = my_email




    with SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(my_email, my_password)
        # SMTPUTF8 signals non-ASCII in headers; Gmail supports it

        #===============================================send message
        now = datetime.now()
        if now.day == 18:
            # get email addresses
            # load_email.get_emails()
            emails = read_emails_from_csv()

            # load quotes from file
            get_quotes_file()  # get content from quotes.txt
            todays_quote = quotes_list[random.randint(0, len(quotes_list))]

            msg["To"] = 'oladipo.bankole@gmail.com'
            msg["Subject"] = 'Your Monthly Spark✨'  # emojis OK
            body = f'{todays_quote['quote']}\n\n~{todays_quote['author']}'
            msg.set_content(body)  # plain text; can include emojis too
            # for n in emails:
            #     msg["To"] = n
            #     msg["Subject"] = 'Your Monthly Spark✨'  # emojis OK
            #     body = f'{todays_quote['quote']}\n\n~{todays_quote['author']}'
            #     msg.set_content(body)  # plain text; can include emojis too
        #==========================================================

        server.send_message(msg, mail_options=["SMTPUTF8"])

    send_email()
    # with SMTP("smtp.gmail.com", 587, timeout=30) as s:
    #     s.starttls()
    #     s.login(my_email, my_password)



# def send_email(to_email, subject, body):
#     with SMTP("smtp.gmail.com", 587, timeout=30) as connection:  # smtp(sender's hostmail,
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs=to_email,
#                             msg=f'Subject:{subject}\n\n{body}'
#                             )




   # send_email(','Your Monthly Spark✨',body)