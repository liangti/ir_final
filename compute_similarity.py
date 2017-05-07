import re
import json
import operator
import math
import nltk
import shelve
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def get_ingredient():
    
    with open("data_sample.json", 'r') as file:
        data = json.load(file)

    ingredient = {}
    tokenizer = RegexpTokenizer(r'\w+')
    stop = set(stopwords.words('english'))
    stop.update(['tsp', 'oz', 'tsk', 'cut', 'g', 'into'])

    d = shelve.open("recipe_similarity")
    
    for item in data:
        ing_list = data[item]['Ingredients']
        ing_name=[]
        for ing in ing_list:
            output = re.sub(r'\d+', '', ing['Name'])
            token = [i.lower() for i in tokenizer.tokenize(output) if i.lower() not in stop]
            ing_name += token
        if ing_name != []:
            ingredient[data[item]['Title']] = ing_name

    for recipe_id in ingredient.keys():
        top5 = recipe_top_5(recipe_id, ingredient)
        d[recipe_id] = top5
        
def cosine_similarity(ing_list1, ing_list2):
    temp = len(ing_list1) * len(ing_list2)
    match_count = count(ing_list1, ing_list2)
    return float(match_count) / math.sqrt(temp)

def count(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2))

def recipe_top_5(recipe_id, all_ing_list):

    ing_similarity = {}

    ing_list = all_ing_list[recipe_id]
    for title in all_ing_list.keys():
        if title == recipe_id:
            continue
        similarity = cosine_similarity(ing_list, all_ing_list[title])
        ing_similarity[title] = similarity + ing_similarity.get(title, 0)

    sorted_tups = sorted(ing_similarity.items(), key=operator.itemgetter(1), reverse=True)
    top_5 = [sorted_tups[0][0], sorted_tups[1][0], sorted_tups[2][0], sorted_tups[3][0], sorted_tups[4][0]]

    return ",".join(top_5)

get_ingredient()
