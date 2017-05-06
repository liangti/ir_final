from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()



def es_query(query, ingradient='', category='Sauces', instruction=''):
    

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
            "query":      query,
            "operator":  "or",
            "fields":     ["Title"]
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

        print item['_source']['PhotoUrl']
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
        output.append(cur)
        count+=1
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
# es_query('sauce',instruction='oil')
