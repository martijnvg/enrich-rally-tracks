GET /

DELETE /rally-metrics*

GET /rally-metrics*/_search

GET /rally-metrics*/_search
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "task": "insert-messages-with-enrich-pipeline"
                    }
                },
                {
                    "match": {
                        "name": "service_time"
                    }
                },
                {
                    "match": {
                        "sample-type": "normal"
                    }
                },
                {
                    "match": {
                        "meta.tag_bla": "1"
                    }
                }
            ]
        }
    },
    "size": 0,
    "aggs": {
        "ingest_took": {
            "percentiles": {
                "field": "meta.ingest_took"
            }
        },
        "took": {
            "percentiles": {
                "field": "meta.took"
            }
        }
    }
}

GET /users/_mapping