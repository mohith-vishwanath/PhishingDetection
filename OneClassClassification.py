import pandas as pd
from sklearn import svm
import csv

email_path = "datasets/fradulent_emails_converted.csv"
url_contents = [".com","https","www",".edu","//"]

emails_file = pd.read_csv(email_path)

for rows, columns in emails_file.iterrows():
