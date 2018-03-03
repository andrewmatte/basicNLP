print("importing libraries")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from os import listdir

print("looking for files")
positives = listdir('../positives')
negatives = listdir('../negatives')

#cleanup for a OSX
positives.remove('.DSstore')
negatives.remove('.DSstore')

print("found " + str(len(positives)) + " positive documents to work with")
print("found " + str(len(negatives)) + " negative documents to work with")
print("arranging data")
data = [['warLanguageLabel', 'text']]
for pos in positives:
    data.append([1,open('../positives/' + pos,'r').read()])


for neg in negatives:
    data.append([0,open('../negatives/' + neg,'r').read()])



all_text = [x[1] for x in data[1:]]

print("vectorization setup")
vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='char',
    ngram_range=(3, 7),
    max_features=100)


print("vectorization")
vectorizer.fit(all_text)
X = vectorizer.transform(all_text)


y = [x[0] for x in data[1:]]
classifier = LogisticRegression()
classifier.fit(X, y)
print("classification success rate: " + str(int(1000*classifier.score(X,y))/10) + "%")
