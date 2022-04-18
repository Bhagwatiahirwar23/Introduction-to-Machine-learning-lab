import pandas as pd 
import pdb
msg = pd.read_csv('naivetext1.csv',names = ['message','label'])  #name of the cols
print(msg)
msg['labelnum'] = msg.label.map({'pos' :0 ,'neg' :1})
x = msg.message
y = msg.labelnum

"""from sklearn.modal_selection import train_test_split
xtrain,xtest,ytrain,ytext = train_test_split(x,y)

from sklearn.feature_extraction.text import countVectorizer
count_vect = countVectorizer()
print(len(xtrain))

xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm  = count_vect.transform(xtrain)
print(xtest_dtm)

df = pd.DataFrame(xtrain_dtm.toarray(),columns=count_vect.get_feature_name_out())
print(df)
from sklearn.naivebayes import multinomialNB
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(xtrain_dtm,ytrain)
predicted = clf.predict(xtest_dtm)
from sklearn import metrics
print('Accuracy metrics')
print('Accuracy of the classifer is',metrics.accuracy_score(ytest,predicted))
print('Confusion matrix')
print(metrics.confusion_matrix(ytest,predicted))
print('Recall and Precison ')
print(metrics.recall_score(ytest,predicted))
print(metrics.precision_score(ytest,predicted))
pdb.set_trace()"""

