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
                            ['minutes','min','h']
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
        "wiki_type":{
            "properties":{
                "title":{
                    "type":"text",
                    "analyzer":"my_synonym",
                },
                "text":{
                    "type":"text",
                    "analyzer":"my_synonym",
                },
                "starring":{
                    "type":"string",
                    "analyzer":"my_synonym",
                },
                "categories":{
                    "type":"string",
                    "analyzer":"my_synonym" ,
                },
                "runtime":{
                    "type":"long",
                    "analyzer":"my_stop",
                },
            }
        }

    }
}

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

corpus='movie2'

es.indices.delete(index=corpus)
es.indices.create(index=corpus, ignore=400, body=create_body)

with open("test_corpus.json", 'r') as file:
    data = json.load(file)
    
count=0
for item in data:
    print item
    #print data[item]
#     print data[item]['runtime']
    if len(data[item]['runtime'])==0: 
        data[item]['runtime']="30 minutes"
        
#     if len(data[item]['runtime'])<6: 
#         #print 'fuck'
#         data[item]['runtime']=data[item]['runtime'][0]
#     run_list=data[item]['runtime'].split('minutes')
#     if len(run_list)==0: data[item]['runtime']=0
#     else: data[item]['runtime']=run_list[0]
#     print data[item]['runtime']
    if len(data[item]['runtime'])<6: 
        #print 'fuck'
        data[item]['runtime']=data[item]['runtime'][0]
    if type(data[item]['categories'])==type(list):
        data[item]['categories']=" ".join(data[item]['categories'])
    data[item]['starring']=" ".join(data[item]['starring'])
    run_list=re.findall(r"\d+\.?\d*",data[item]['runtime'])
#     print data[item]['runtime']
    if len(run_list)==0:
        data[item]['runtime']=30
    else:
        data[item]['runtime']=int(float(run_list[0]))
#     es.index(index='movie', doc_type='movie', id=item, body=(data[item]))

# actions = [
# {
# "_index": "movie",
# "_id": 42,
# "_source": {
#         "title": data[item]['title'],
#         "text": data[item]['text'],
#         "location": data[item]['location'],
#         "categories": data[item]['categories'],
#         "director": data[item]['director'],
#         "location": data[item]['location'],
#         "starring": data[item]['starring'],
#         "time": data[item]['time'],
#         "runtime": data[item]['runtime']
#     }
# }
#            for item in data
# ]
# helpers.bulk(es, actions, index="movie")

action=[]
for item in data:
    #print data[item]['title']
    action.append(data[item])
    if len(action)==500:
        helpers.bulk(es, action, index=corpus, doc_type="wiki_type", stats_only=True)
        action=[]
     
helpers.bulk(es, action, index=corpus, doc_type="wiki_type", stats_only=True)
action=[]
