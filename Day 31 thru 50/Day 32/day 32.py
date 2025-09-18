from smtplib import *
#============== Email SMTP and datetime module
#=========== Sending emails using Python!
#Module: Email SMTP (smtplib). Prepackaged with python and helps send email
#        Datetime. tracks current date
import smtplib
#gmail's smtp host> smtp.gmail.com
#hotmail> smtp.live.com
#outlook> outlook.office365.com
#yahoo> smtp.mail.yahoo.com
# Understanding how email works
#======================Working with Date Time lib
def date_time_module():
    from  datetime import datetime
    now = datetime.now()

    print ('Year: ',now.year)
    print ('Month: ',now.month)
    print ('Day: ',now.day)
    print ('Hour: ',now.time().hour)
    print ('Day of week: ',now.weekday())

    dob = datetime(year=1990, month=10, day=19)
    print ('random date of birth: ', dob)
date_time_module()

def emailer_test():
    from dotenv import load_dotenv
    import os
    load_dotenv(dotenv_path="Birthday Wisher (Day 32) start/.env")
    my_email = os.getenv("MY_EMAIL")
    my_password = os.getenv("MY_PASSWORD")
    to_email = 'oladipo.bankole@gmail.com'

    with SMTP("smtp.gmail.com", 587, timeout=30) as connection:  # smtp(sender's hostmail,
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg='Subject:Hello World\n\nTHis is the body of my email'
                            )
emailer_test()