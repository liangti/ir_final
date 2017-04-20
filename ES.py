from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()



def es_query(query, starring, genre, run1, run2):
    if starring=='': starring='.*'
    if run1=='': run1=0
    else: run1=int(run1)
    if run2=='': run2=1000000
    else: run2=int(run2)
    print genre
    if genre=='default': 
        genre="films"
#         genre=['comedy', 'romance', 'thriller', 'mystery', 'crime', 'drama', 'musical', 'documentary', 'western', 'animation']
#     else: genre=[genre]
    print run1, run2
    print query
    print starring
    movies = es.search(index="movie", body={
    
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
        "filter": [
                 { "range": { "runtime": { 
                     "gte": run1,
                     "lte": run2 }}},
                   {"match": { "categories": genre}}
             ],
#        "must":[{ "match": { "categories": genre}}],
       "must": 
        {
          "multi_match" : {
            "query":      query,
            "operator": "and",
            "fields":     [ "title", "text" ],
            "minimum_should_match": "50%" 
          }
        
        },
        "should":
        {
          "multi_match" : {
            "query":      starring,
            "operator": "and",
            "fields":     [ "starring"],
            "minimum_should_match": "100%" 
          }
        
        }
      
            
    }
  },
      "highlight" : {
        "fields" : {
            "text" : {}
        }
    }
    
    })
    output=[]
    count=1
    for item in movies['hits']['hits']:
#         print run1,run2,item['_source']["runtime"]
        cur=[item['_source']["title"],item['_source']["text"],item['_source']["language"],item['_source']["country"],item['_source']["director"],item['_source']["location"],item['_source']["starring"],item['_source']["time"],item['_source']["runtime"],item['_source']["categories"]]
        content=cur[1]
        if len(content)>300:
            content=content[0:300]+"..."
        cur.append(item['highlight']['text'])
        cur[1]=content
        cur.append(str(count))
        cur.append(item['_score'])
        output.append(cur)
        count+=1
        #print item['_source']["title"]
    print len(output)
    return output,len(output)

 
# for item in movies['hits']['hits']:
#     print item['_source']['title'],'title'
#     
# res = es.get(index="movie", doc_type="movie")
# print(res)
# es_query('film', '', 'default','0','1000')