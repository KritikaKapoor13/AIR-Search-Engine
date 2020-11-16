from elasticsearch import Elasticsearch
es=Elasticsearch([{'host':'localhost','port':9200}])
import time
t1=time.time()
# res= es.search(index='archive',size=25,body={"query": {"wildcard": {
#       "Snippet": {"value":"pre*ent"}}}})
# res=es.search(index='archive',size=25,body={"query": {
#     "query_string": {
#       "query": "(president trump) AND (joe biden)",
#       "default_field": "Snippet",
#       "auto_generate_synonyms_phrase_query":False
#     },
# }})
# res= es.search(index='archive',request_timeout=30,size=94858,body={
#   "query": {
#       'bool':
#     {"must": [
#         {"match":
#       {"Snippet": {
#         "query": "emergenci",
#         "fuzziness": "AUTO"
#       }
#     }},
#         {"match":
#       {"Snippet": {
#         "query": "fundin",
#         "fuzziness": "AUTO"
#       }
#     }}
#     ]
#   }}
# })
# res= es.search(index='archive',request_timeout=30,size=94858,body={ "query": {
#     "match": {
#       "Snippet": {
#         "query": "emergenci",
#         "fuzziness": "AUTO"
#       }
#     }
#   }
# })
# res= es.search(index='archive',size=94858,body={"query": {"wildcard": {
#       "Snippet": {"value":"sch*zene*ger"}}}})
res=es.search(index='archive',size=94858,body={"query": {
    "query_string": {
      "query": "war AND (iraq OR afghanistan)",
      "default_field": "Snippet",
      "auto_generate_synonyms_phrase_query":False
    },
}})
# res= es.search(index='archive',size=94858,body={'query':{
#             'bool':{
#                 'must':{'bool':{
#                     'should':[{
#                         'match_phrase':{
#                             'Snippet':'environmental issue'
#                             }
#                         },
                        # {"wildcard": {
                        #     "Snippet": 
                        #     {"value":"euro*n"}}
                        # }
#                         {
                        # 'match_phrase':{
                        #     'Snippet':'political issue'
                        #     }
                        # }
#                         # {'bool':
#                         #     {'should':
#                         #     [
#                         #         {
#                         #         'match':{
#                         #             'Snippet':'iran'
#                         #             }
#                         #         },
#                         #         {
#                         #         'match':{
#                         #             'Snippet':'afghanistan'
#                         #             }
#                         #         }
#                         #     ]
#                         #     }
#                         # }
#                         ]
#                     }}}
#                 }})
# res= es.search(index='archive',request_timeout=30,size=94858,body={'query':{
#             'bool':{
#                     'must':[
#                         { "match": {
#                                 "Snippet": {
#                                     "query": "wasingtonn",
#                                     "fuzziness": "AUTO"
#                                 }
#                                 }
#                             },
#                               {                  'match_phrase':{
#                             'Snippet':'tom steyer'
#                             }
#                         }   
#                         ]
#                     }
# }})

t2=time.time()
import sys
print(res['hits']['total']," ",len(res['hits']['hits']))
t3=time.time()
f = open(r'text1.txt', 'w',encoding='utf-8')
for i in res['hits']['hits']:
    j=i['_source']
    f.write(j['Snippet'])
    f.write('\n')
f.close()
t4=time.time()
print(t2-t1)
print(t4-t3)