'''
Created on Apr 2, 2017

@author: uuisafresh
'''
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import numpy as np
import json
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
                    "analyzer":"my_synonym"


                },

                "Ing_List" :{
                    "type": "nested",
                    "properties":{
                    "Name":{"type": "text"},
                    "Unit":{"type": "text"},
                    "Quantity":{"type": "float"},
                    "PreparationNotes":{"type": "text"}
                    },
                    "analyzer":"my_synonym",
                },
                          
                "Ing_Name" :{
                    "type": "text",
                    "analyzer":"my_synonym"
                },
                "SVD" :{
                    "type": "text"
                }
            }
        }

    }
}

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

corpus='reciption2'

es.indices.delete(index=corpus)

es.indices.create(index=corpus, ignore=400, body=create_body)

with open("data_sample.json", 'r') as file:
    data = json.load(file)

n2i=dict()
count=0
for item in data:
    ings=data[item]['Ingredients']
    for ing in ings:
        if not ing['Name'] in n2i: 
            n2i[ing['Name']]=count
            count+=1
     
print len(n2i),'len_dictionary'
count=0
matrix=np.zeros((len(data),len(n2i)))
for item in data:
    ings=data[item]['Ingredients']
    for ing in ings:
        index=n2i[ing['Name']]
        matrix[count][index]=1
        print index
    count+=1
print sum(matrix[0])
U, S, V = np.linalg.svd(matrix)
print U.shape,S.shape, V.shape,'shape'

count=0
for item in data:
    ings=data[item]['Ingredients']
    ing_list=[]
    ing_name=''
    for ing in ings:
        ing_list.append([ing['Name'],ing['Unit'],str(ing['Quantity']),ing['PreparationNotes']])
        ing_name+=ing['Name']
    data[item]['Ing_List']=ing_list
    data[item]['Ing_Name']=ing_name
    SVD_str=[str(i) for i in U[count]]
    print len(SVD_str),'1'
    data[item]['SVD']=' '.join(SVD_str)
    print len(data[item]['SVD'].split()),"2"
    count+=1

#     data[item]['Photo']='https://bigoven-res.cloudinary.com/image/upload/shit-on-a-shingle-recipe-'+item+'.jpg'
#     print ing_name

action=[]
for item in data:
    #print data[item]['title']
    action.append(data[item])
    #print data[item]['Title']
    #print len(action)
    if len(action)==500:
        helpers.bulk(es, action, index=corpus, doc_type="food_type")
        action=[]

if len(action)!=0:
    helpers.bulk(es, action, index=corpus, doc_type="food_type")
action=[]
