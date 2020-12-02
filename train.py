from preprocess import DataPre
import csv
import time
import nltk 
from matplotlib import pyplot


def feature_vector(tweet):
    vocab = set(tweet)
    vector = {}
    for word in features:
        vector['contains(%s)' % word] = (word in vocab)
    return vector

def wordFrequency(X_train):
    vocabulary = []
    
    for (words, sentiment) in X_train:
        vocabulary.extend(words)

    frequency = nltk.FreqDist(vocabulary)
    frequency.plot(50, cumulative=False)
    features = frequency.keys()
    
    return features


trainingData = []
testData = []

# read from csv
with open("tweets.csv", 'r') as csvfile:
    line = csv.reader(csvfile, delimiter=',', quotechar="\"")
    for row in line:
        trainingData.append({"tweet": row[0], "label": row[1]})

with open("testtweets.csv", 'r') as csvfile:
    line = csv.reader(csvfile, delimiter=',', quotechar="\"")
    for row in line:
        testData.append({"tweet": row[0], "label": row[1]})


dataPreObject = DataPre()
X_train = dataPreObject.initialize(trainingData)
X_test = dataPreObject.initialize(testData)


# set features to the frequency list
features = wordFrequency(X_train)

# training features and test features
trainingFeatures = nltk.classify.apply_features(feature_vector, X_train)
testingFeatures = nltk.classify.apply_features(feature_vector, X_test)

model = nltk.NaiveBayesClassifier.train(trainingFeatures)

# test and accuracy
count_of_correct = 0
total = 0
for tweet in X_test:
    print("tweet: ", tweet[0])
    print("actual: ",tweet[1])
    total += 1
    result = model.classify(feature_vector(tweet[0]))
    print("result:", result)
    if result == tweet[1]:
        count_of_correct += 1

print("accuracy of: ", 100*(count_of_correct/total), "%")

