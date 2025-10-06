from smtplib import SMTP
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime
import os
import csv
import random
from typing import List, Dict
from get_gmail_addresses import get_emails

# ----------------- Config -----------------
CSV_PATH = "gmail_addresses.csv"
QUOTES_PATH = "quotes.txt"
SERIES_SUBJECT = "Your Monthly Spark ✨"
SEND_DAY = 0  # send on the 18th of each month
DRY_RUN = False  # set True to print instead of send
# ------------------------------------------

# load env
load_dotenv()
MY_EMAIL = os.getenv("SEC_EMAIL")
MY_PASSWORD = os.getenv("SEC_PASSWORD")


def read_emails_from_csv(path: str = CSV_PATH) -> List[str]:
    get_emails()
    emails: List[str] = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            if row and row[0].strip():
                emails.append(row[0].strip().lower())
    return emails


def load_quotes(path: str = QUOTES_PATH) -> List[Dict[str, str]]:
    quotes: List[Dict[str, str]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if " - " in s:
                quote, author = s.rsplit(" - ", 1)
                quotes.append({
                    "quote": quote.strip('" ').strip(),
                    "author": author.strip()
                })
    if not quotes:
        raise RuntimeError("No quotes parsed from quotes.txt")
    return quotes


def send_monthly_quotes():
    if not MY_EMAIL or not MY_PASSWORD:
        raise RuntimeError("Missing SEC_EMAIL or SEC_PASSWORD in .env")

    # Only run on the configured day
    today = datetime.now()
    if today.weekday() != SEND_DAY:
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(f"Today is {day_names[today.weekday()]}. Not sending today. It only sends on {day_names[SEND_DAY]} of the week.")
        return

    emails = read_emails_from_csv()
    quotes = load_quotes()
    chosen = random.choice(quotes)
    body = f"{chosen['quote']}\n\n~{chosen['author']}"


    sent_count = 0

    with SMTP("smtp.gmail.com", 587, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(MY_EMAIL, MY_PASSWORD)

        for addr in emails:
            # Build a fresh message for each recipient
            msg = EmailMessage()
            msg["From"] = MY_EMAIL
            msg["To"] = addr
            msg["Subject"] = SERIES_SUBJECT
            msg.set_content(body)

            if DRY_RUN:
                print(f"[DRY RUN] Would send to: {addr}")
            else:
                server.send_message(msg, mail_options=["SMTPUTF8"])
                print(f"Sent to: {addr}")
                sent_count += 1

    print(f"Done. Total sent: {sent_count}")


# if __name__ == "__main__":
send_monthly_quotes()
