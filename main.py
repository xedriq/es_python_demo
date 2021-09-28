from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, connections, Q, index

# connections.create_connection(hosts=['92.168.3.225:9200'], timeout=60)


es = Elasticsearch('192.168.3.225:9200')

query = {
    "bool": {
        "must_not": [
            {
                "match": {
                    "content": "covid"
                }
            }
        ],
        "must": [
            {
                "match": {
                    "title": "duterte"
                }
            }
        ]
    }
}

res = es.search(index="articles_jan_2021", query=query,
                track_total_hits=True)

for hit in res['hits']['hits']:
    print(hit["_source"])
    
print("Got %d Hits:" % res['hits']['total']['value'])
