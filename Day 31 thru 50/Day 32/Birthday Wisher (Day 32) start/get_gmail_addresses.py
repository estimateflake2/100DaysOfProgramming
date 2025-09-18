import re
import os
import imaplib
import email
from email.utils import getaddresses
import csv
import time
from dotenv import load_dotenv

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
ALLOWED_DOMAINS = {
    "gmail.com", "googlemail.com",  # include both just in case
    "yahoo.com",
    "hotmail.com", "outlook.com", "live.com", "msn.com",
    "aol.com", "icloud.com", "protonmail.com", "gmx.com",
}

DO_NOT_EMAIL = {
    "3drealtypm@gmail.com",
    "aokanlawoh@gmail.com",
    "celticotast@gmail.com"
}

load_dotenv()
GMAIL_USER = os.getenv("SEC_EMAIL")
APP_PASSWORD = os.getenv("SEC_PASSWORD")

IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
BATCH_SIZE = 500
SLEEP_BETWEEN_BATCHES = 0.5


def normalize_email(addr: str) -> str:
    """Lowercase, strip spaces, canonicalize gmail-style plus tags and dots."""
    if not addr:
        return ""
    addr = addr.strip().lower()
    if "@" not in addr:
        return addr
    local, domain = addr.split("@", 1)
    # Treat googlemail.com as gmail.com
    if domain in ("gmail.com", "googlemail.com"):
        # Drop anything after '+'
        if "+" in local:
            local = local.split("+", 1)[0]
        # Remove dots in the local part
        local = local.replace(".", "")
        domain = "gmail.com"
    else:
        # Light normalization for other providers: drop +tag only
        if "+" in local:
            local = local.split("+", 1)[0]
    return f"{local}@{domain}"


def load_blocklist(path: str = "do_not_email.txt") -> set:
    s = set()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    s.add(normalize_email(line))
    # Merge inline set
    for addr in DO_NOT_EMAIL:
        s.add(normalize_email(addr))
    return s


def is_valid_email(addr: str, blocklist: set) -> bool:
    addr_n = normalize_email(addr)
    if not EMAIL_REGEX.match(addr_n):
        return False
    domain = addr_n.split("@", 1)[1]
    if domain not in ALLOWED_DOMAINS:
        return False
    if addr_n in blocklist:
        return False
    return True


def connect():
    imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
    imap.login(GMAIL_USER, APP_PASSWORD)
    return imap


def fetch_uids(imap):
    imap.select("INBOX")
    typ, data = imap.uid("search", None, "ALL")
    if typ != "OK":
        raise RuntimeError("UID search failed")
    return data[0].split()


def fetch_headers_batch(imap, uids_batch):
    fetch_items = b",".join(uids_batch)
    typ, data = imap.uid(
        "fetch",
        fetch_items,
        '(BODY.PEEK[HEADER.FIELDS (FROM TO CC BCC)])'
    )
    if typ != "OK":
        raise RuntimeError("UID fetch failed")
    return data


def extract_emails_from_headers(raw_blocks, blocklist):
    emails = set()
    for i in range(0, len(raw_blocks), 2):
        if not isinstance(raw_blocks[i], tuple):
            continue
        msg = email.message_from_bytes(raw_blocks[i][1])
        fields = []
        if msg.get("From"): fields.append(msg.get("From"))
        if msg.get("To"):   fields.append(msg.get("To"))
        if msg.get("Cc"):   fields.append(msg.get("Cc"))
        if msg.get("Bcc"):  fields.append(msg.get("Bcc"))
        for _, addr in getaddresses(fields):
            if addr and is_valid_email(addr, blocklist):
                emails.add(normalize_email(addr))
    return emails


def write_csv(emails, path="gmail_addresses.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["email"])
        for addr in sorted(emails):
            writer.writerow([addr])
    print("Saved:", path)


def get_emails():
    if not GMAIL_USER or not APP_PASSWORD:
        raise RuntimeError("Missing SEC_EMAIL or SEC_PASSWORD in .env")

    blocklist = load_blocklist("do_not_email.txt")

    all_emails = set()
    imap = connect()
    try:
        uids = fetch_uids(imap)
        print("Total messages:", len(uids))
        for start in range(0, len(uids), BATCH_SIZE):
            end = min(start + BATCH_SIZE, len(uids))
            batch = uids[start:end]
            data = fetch_headers_batch(imap, batch)
            new_set = extract_emails_from_headers(data, blocklist)
            all_emails.update(new_set)
            #print(f"Processed {end}/{len(uids)}; unique emails so far: {len(all_emails)}")
            time.sleep(SLEEP_BETWEEN_BATCHES)
    except Exception as e:
        print("Error:", e)

    else:
        # Only runs if no exception occurred — PyCharm considers this reachable
        write_csv(all_emails)

    finally:
        try:
            imap.logout()
        except Exception:
            pass

    write_csv(all_emails)


