import csv

text_file_path = "datasets/fradulent_emails.txt"

file_pointer = open(text_file_path,"r")
line = file_pointer.readlines()

header_contents = dict()

def InitialiseDictinary():
    header_contents[email_from] = "NA"
    header_contents[return_path] = "NA"
    header_contents[reply_to] = "NA"
    header_contents[sent_to] = "NA"
    header_contents[subject] = "NA"
    header_contents[x_mailer] = "NA"
    header_contents[mime_version] = "NA"
    header_contents[content_type] = "NA"
    header_contents[content_transfer] = "NA"
    header_contents[x_mime_autoconverted] = "NA"
    header_contents[status] = 0
    header_contents[message] = "NA"


destination_file = open("datasets/fradulent_emails_converted.csv","w+")

all_emails = []
total_lines = len(line)
emails_count = 0

#Dict Keys
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

csv_writer = csv.writer(destination_file)
csv_writer.writerow([email_from,return_path,reply_to,sent_to,subject,x_mailer,mime_version,content_type,content_transfer,x_mime_autoconverted,status,message])

InitialiseDictinary()

for current_line in range(total_lines):
    if line[current_line][:6].__contains__("From r") or line[current_line][:8].__contains__("X-Sieve:") or line[current_line][:11].__contains__("Message_Id:") or line[current_line][:5].__contains__("Date:"):
        continue
    else:
        if line[current_line][:13].__contains__("Return-Path:"):
            header_contents[return_path] = line[current_line][14:]
        elif line[current_line][:5].__contains__("From:"):
            header_contents[email_from] = line[current_line][6:]
        elif line[current_line][:9].__contains__("Reply-To:"):
            header_contents[reply_to] = line[current_line][10:]
        elif line[current_line][:3].__contains__("To:"):
            header_contents[sent_to] = line[current_line][4:]
        elif line[current_line][:8].__contains__("Subject:"):
            header_contents[subject] = line[current_line][9:]
        elif line[current_line][:9].__contains__("X_Mailer:"):
            header_contents[x_mailer] = line[current_line][10:]
        elif line[current_line][:13].__contains__("MIME-Version:"):
            header_contents[mime_version] = line[current_line][14:]
        elif line[current_line][:13].__contains__("Content-Type"):
            header_contents[content_type] = line[current_line][14:]
        elif line[current_line][:26].__contains__("Content-Transfer-Encoding"):
            header_contents[content_transfer] = line[current_line][27:]
        elif line[current_line][:21].__contains__("X-MIME-Autoconverted:"):
            header_contents[x_mime_autoconverted] = line[current_line][22:]
        elif line[current_line][:7].__contains__("Status:"):
            header_contents[status] = line[current_line][8:]
            current_line += 1
            header_contents[message] = ""
            while line[current_line][:6].__contains__("From r") == False:
                header_contents[message] += " " + str(line[current_line])
                current_line += 1
                if current_line >= total_lines:
                    break
            emails_count += 1
            csv_writer.writerow([header_contents[email_from],header_contents[return_path],header_contents[reply_to],header_contents[sent_to],header_contents[subject],header_contents[x_mailer],
                             header_contents[mime_version],header_contents[content_type],header_contents[content_transfer],header_contents[x_mime_autoconverted],
                             header_contents[status],header_contents[message]])
            InitialiseDictinary()
            all_emails.append(header_contents)
print("Total Emails : " + str(emails_count))
print("Done writing to csv file")




