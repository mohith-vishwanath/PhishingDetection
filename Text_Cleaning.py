import re
import csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

# CONSTANTS
email_from = "from"
return_path = "return path"
reply_to = "reply to"
sent_to = "sent to"
subject = "subject"
x_mailer = "X Mailer"
mime_version = "MIME Version"
content_type = "content type"
content_transfer = "content transfer"
x_mime_autoconverted = "X MIME Autoconverted"
status = "status"
message = "message"

url_contents = [".com","https","www.",".edu","//"]

files = "datasets/fradulent_emails_converted.csv"
destination_emails = "datasets/Final Files/fraud_emails.csv"
destination_links = "datasets/Final Files/fraud_links.csv"
excel_file = pd.read_csv(files)

destination = open(destination_emails, "w+")
dest = open(destination_links,"w+")
links_writer = csv.writer(dest)

links_writer.writerow(["links"])
writer = csv.writer(destination)
writer.writerow([email_from, return_path, sent_to, reply_to])

# Gather all the links and emails from the document
for rows, columns in excel_file.iterrows():
    sent_by = re.split(" <| |>", str(columns[email_from]))
    return_address = re.split(" <| |>", str(columns[return_path]))
    sent_address = re.split(" <| |>", str(columns[sent_to]))
    reply_address = re.split(" <| |>", str(columns[reply_to]))

    for email in sent_by:
        if email.__contains__("@") == True:
            final_sent_by = email
    for email in return_address:
        if email.__contains__("@") == True:
            final_return_address = email
    for email in sent_address:
        if email.__contains__("@") == True:
            final_sentaddress = email
    for email in reply_address:
        if email.__contains__("@") == True:
            final_replyaddress = email

    email_body = str(columns[message])
    for words in email_body:
        for x in url_contents:
            if words.__contains__(x):
                links_writer.writerow([words])
                print(words)
                break

    writer.writerow([final_sent_by, final_return_address, final_sentaddress, final_replyaddress])
