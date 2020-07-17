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
- 007
- gcptest101 - Created for NextGenLabs demo 18 July 2020

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
