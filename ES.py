from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()



def es_query(title, ingradient='', category='Sauces', instruction=''):
    

    recipts = es.search(index="reciption2", body={
    
    "size" : 2400,
    "sort" : "_score",
    "query": {
    "bool": {
#       "must":{
#               "terms": { "categories": genre}
#               },
#       "must":{
#          
#            "range": { "runtime": { 
#                    "gt": run1,
#                    "lte": run2
#                    }}
#               
#           },
#         "filter": [
#                  { "range": { "runtime": { 
#                      "gte": run1,
#                      "lte": run2 }}},
#                    {"match": { "categories": genre}}
#              ],
#        "must":[{ "match": { "categories": genre}}],
       "should": 
        {
          "multi_match" : {
            "query":      title,
            "operator":  "or",
            "fields":     ["Title"]
          }
        },
        "should":
        {
            
         "multi_match" : {
            "query":      instruction,
            "operator":  "or",
            "fields":     ["Instructions"]
          }
        },
             "should":
        {
            
         "multi_match" : {
            "query":      category,
            "operator":  "or",
            "fields":     ["Category"]
          }
        },
             "should":
        {
            
         "multi_match" : {
            "query":      instruction,
            "operator":  "or",
            "fields":     ["Instructions"]
          }
        }
            
    }
  }
#       "highlight" : {
#         "fields" : {
#             "text" : {}
#         }
#     }
    
    })
    output=[]
    count=1
    for item in recipts['hits']['hits']:
        #print item
        
        output.append(item)
        #print item['_score']
        #print item['_source']['Instructions']
#         print item['_source']["Title"]
#         print item['_source']["Category"]
#         print item['_source']["Ing_Name"]
        #print "*********"
    #print len(output)
    return output,len(output)

 
# for item in movies['hits']['hits']:
#     print item['_source']['title'],'title'
#     
# res = es.get(index="movie", doc_type="movie")
# print(res)
es_query('sauce',instruction='oil')
