[![Build Status](https://travis-ci.com/srujandeshpande/AQ-Cloud-Site.svg?branch=master)](https://travis-ci.com/srujandeshpande/AQ-Cloud-Site)  
# AQ-Cloud-Site
PES Innovation Lab's Internship 2020 Project - Air Quality Cloud Site Visualization  
[Presentation Link](https://drive.google.com/file/d/1UyhHgBk02pf-diae1FCsIPtTNQCV3dE_/view?usp=sharing)

## How to run
- Intall the packages using `pip install -r requirements.txt`
- Run using `flask run`

## Running Gunicorn (Production Server)
`gunicorn app:app --bind 0.0.0.0:8000` or  
`gunicorn filename:app --bind 0.0.0.0:8000`

## Misc data
- Kibana port 5601
- Elasticsearch port 9200


## Mock Sensor IDs
- gcptest004
- 005
- 006
- 007, 008 for Demo
- loadtest101 load testing

### When creating new sensor make new index
send directly to Elasticsearch  
URL: http://35.209.87.44:9200/<new device id (index name)>  
Ex: http://35.209.87.44:9200/gcptest007
```json
{
    "mappings": {
        "properties": {
            "timestamp": {
                "type": "date"
            },
            "location": {
                "type": "geo_point"
            }
        }
    }
}
```

### Graphs on Kibaba
1. Create index pattern
2. **DO NOT** select timestamp field when it asks
3. Go to Visualization and choose line graph
4. Y axis - Average - Field choose any 1
5. Buckets - X axis - Aggregation - Date Histogram - timestamp - 5s (or anything)


### Docker commands for Flask Server
1. docker build --tag aqserver:1.0 .
2. docker run -p 8000:8000 aqserver:1.0


### Docker commands for Mock sensor
1. docker build --tag aqmocksensor:1.0 .
2. docker run aqmocksensor:1.0
