import json
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

def getCorpus(path):

    with open(path) as data_file:
        data = json.load(data_file)

    return data

def prepareIndex():

    data = getCorpus("data_test.json")
    food_list = []

    for key in data.values():
        title = query(key["Title"])
        food_list += title
        for temp in key['Ingredients']:
            food = query(temp['Name'])
            food_list += food

    with open('food.json', 'w') as outfile:
        json.dump(food_list, outfile)

def query(text):
    
    stop_words = set(stopwords.words('english'))
    
    tokens = nltk.word_tokenize(text)
    term = [i.lower() for i in tokens if i.lower() not in stop_words]

    return term

prepareIndex()
