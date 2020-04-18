from nltk import TreebankWordTokenizer
from sklearn import svm, metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

files_path = ["datasets/messages.csv","datasets/emails 2.csv"]
count = 0
split_for_each = [2300,4000]
labels = ['0','1']

waste_symbols = [")","(","*","&","^","-","_","+","=","\\","/","|","%","$","#","@","!","`","~","<",">","?",":",";","[","]","{","}"]

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

training_messages = []
training_labels = []

testing_messages = []
testing_labels = []

for files in files_path:
    file = pd.read_csv(files)
    for rows, columns in file.iterrows():
        text_in_email = columns['message']
        final_set_of_words = ""
        for words in text_in_email:
            if (str(words).isnumeric() == False) and (words not in waste_symbols):
                if words not in stop_words:
                    final_set_of_words += " " + lemmatizer.lemmatize(words,'v')
        if rows < split_for_each[count] :
            training_messages.append(final_set_of_words)
            training_labels.append(columns['label'])
        else:
            testing_messages.append(final_set_of_words)
            testing_labels.append([columns['label']])
    count += 1

print("Data imported")

vector = CountVectorizer(ngram_range=(2,4),tokenizer=TreebankWordTokenizer().tokenize)
count = vector.fit_transform(training_messages)

tfidf = TfidfTransformer()
tfidf_matrix = tfidf.fit_transform(count)

learning_svm = svm.SVC(C=1.0, kernel='poly', degree=3, gamma='auto')
learning_svm.fit(tfidf_matrix, training_labels)

logistic = LogisticRegression(C=0.1,max_iter=1200000,)

learning_bayes = MultinomialNB().fit(tfidf_matrix, training_labels)

learning_logistic = logistic.fit(tfidf_matrix,training_labels)

print("Training Done")

test_data = vector.transform(testing_messages)
test_tfidf = tfidf.transform(test_data)

# SVM Predictor
prediction_svm = learning_svm.predict(test_tfidf)
# Logistic Regression
prediction_logistic = learning_logistic.predict(test_tfidf)
#Bayes Predictor
prediction_bayes = learning_bayes.predict(test_tfidf)

print("-----------------------------------------------------\nNAIVE BAYES CLASSIFIER \n")
print("Accuracy : " + str(round(accuracy_score(testing_labels, prediction_bayes), 3) * 100) + "%")
print(metrics.classification_report(testing_labels, prediction_bayes, target_names=labels,zero_division=0))
print("------------------------------------------------------")

print("------------------------------------------------------\nSUPPORT VECTOR MACHINES \n")
print("Accuracy : " + str(round(accuracy_score(testing_labels, prediction_svm), 3) * 100) + "%")
print(metrics.classification_report(testing_labels, prediction_svm, target_names=labels, zero_division=0))
print("------------------------------------------------------")

print("------------------------------------------------------\nLOGISTIC REGRESSION \n")
print("Accuracy : " + str(round(accuracy_score(testing_labels, prediction_logistic), 3) * 100) + "%")
print(metrics.classification_report(testing_labels, prediction_logistic, target_names=labels, zero_division=0))
print("------------------------------------------------------")