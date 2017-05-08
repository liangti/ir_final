import shelve
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

def recommend_data():

    d = shelve.open("recipe_similarity.dat")
    return d

def es_query(query, ingradient='', category='Sauces', instruction=''):
    

    recipts = es.search(index="reciption2", body={
    
    "size" : 2400,
    "sort" : "_score",
    "query": {
        "bool": {
        "should": [
                { "match": { "Title": query }},
                { "match": { "Category":  query }}
                
            ]
        }
#     "bool": {
# #       
#        "should": 
#         {
#           "multi_match" : {
#             "query":      query,
#             "operator":  "or",
#             "fields":     ["Title"],
#             "minimum_should_match": "0%" 
#           }
#         }
#             
#     }
  }
#       "highlight" : {
#         "fields" : {
#             "text" : {}
#         }
#     }
    
    })
    
    #d = recommend_data()
    
    output=[]
    count=1
    for item in recipts['hits']['hits']:
        #print item
        act_min=str(item['_source']['ActiveMinutes'])+' min'
        if item['_source']['Cuisine']=='': item['_source']['Cuisine']='Unknown'
        cur=[str(count),
             item['_source']["Title"],
             item['_source']["Instructions"],
             item['_source']['PhotoUrl'],
             item['_source']['Ing_Name'],
             item['_source']['Category'],
             item['_source']['LastModified'],
             item['_source']['Cuisine'],
             act_min]

        content=cur[1]
        if len(content)>300:
            content=content[0:300]+"..."
        cur[1]=content
        cur.append(str(count))
        cur.append(item['_score'])
        
        #cur.append(d[item['_source']["Title"]])
        output.append(cur)
        count+=1
#         print item['_score']
#         print item['_source']['Instructions']
#         print item['_source']["Title"]
#         print item['_source']["Category"]
#         print item['_source']["Ing_Name"]
#         print "*********"
    #print len(output)
    return output,len(output)

 
# for item in movies['hits']['hits']:
#     print item['_source']['title'],'title'
#     

es_query('sauce',instruction='oil')
