from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import encode
encode.encode(100000)
data = pd.read_csv('gender_data.csv')
data = data[0:len(data)]
data_feature = data['Name']
data_label = data['Label']
cv = CountVectorizer()

X = cv.fit_transform(data_feature)


x_train, x_test, y_train, y_test = train_test_split(X, data_label, test_size=0.3, random_state=50)

bayes = MultinomialNB()
bayes.fit(x_train, y_train)
result = bayes.predict(x_test)
print(100*accuracy_score(y_test, result))



tree = DecisionTreeClassifier()
tree.fit(x_train, y_train)
result = tree.predict(x_test)
print(100*accuracy_score(y_test, result))

rf = RandomForestClassifier(n_estimators=20)
rf.fit(x_train, y_train)
result = rf.predict(x_test)
print(100*accuracy_score(y_test, result))

gra = GradientBoostingClassifier()
gra.fit(x_train, y_train)
result = gra.predict(x_test)
print(100*accuracy_score(y_test, result))
