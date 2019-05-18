import urllib, json

query = {
  "resource_id": "391792b5-9c0a-48a1-918f-2ee63caa1c54",
  "limit": 10,
  "offset": 20
}

results = urllib.urlopen(
  "http://hub.Healthdata.gov/api/action/datastore_search",
  urllib.quote(json.dumps(query)))

results = json.load(results)

for rec in results["result"]["records"]:
  print rec["hsp_name"]