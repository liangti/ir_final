'''
Created on Apr 2, 2017

@author: uuisafresh
'''
from elasticsearch import Elasticsearch
from elasticsearch import helpers

import json
import re
stop_word=stop_word="a the about above after again against all an and any as at be because before below between both but by cannot could did do down during each few for from further have here he how i if in into it itself let me more he it you most must my myself no nor not of off on once only or other ought our osu . ! ? , ;".split()
create_body= {
    "settings": {
        "analysis": {
            "analyzer": {
                "my_stop": {
                    "type":      "custom",
                    "tokenizer": "standard",
                    "filter": [
                            "lowercase",
                            "asciifolding",
                            "porter_stem",
                            []
                            ]
                },
                "my_synonym": {
                    "type":      "custom",
                    "tokenizer": "standard",
                    "filter":[
                            [
                            "lowercase"
                            "asciifolding"
                            "porter_stem"
                            "synonym"
                            ],
                            stop_word]
                }
            },
            "filter": {
                "synonym" : {
                    "type" : "synonym",
                    "synonym" : ["films,2016,IMAX=>default"],
                    "ignore_case":"true"
                }
            }
        },
    },
    "mappings":{
        "food_type":{
            "properties":{
                "Title":{
                    "type":"text",

                },
                "Ing_Name" :{
                    "type":"text",
                    "analyzer":"my_synonym",
                },
            }
        }

    }
}

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

corpus='reciption2'
es.indices.delete(index=corpus)
es.indices.create(index=corpus, ignore=400, body=create_body)

with open("data_test.json", 'r') as file:
    data = json.load(file)

count=0
for item in data:
    ing_list=data[item]['Ingredients']
    ing_name=''
    for ing in ing_list:
        ing_name+=ing['Name']
    data[item]['Ing_Name']=ing_name

action=[]
for item in data:
    #print data[item]['title']
    action.append(data[item])
    if len(action)==500:
        helpers.bulk(es, action, index=corpus, doc_type="food_type", stats_only=True)
        action=[]

if len(action)!=0:
    helpers.bulk(es, action, index=corpus, doc_type="food_type", stats_only=True)
action=[]
