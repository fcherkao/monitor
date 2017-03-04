import requests, json

# Replace 'localhost' with your FQDN and certificate CN
# for SSL verification
request_url = "https://192.168.122.242:5665/v1/objects/services"
headers = {
    'Accept': 'application/json',
    'X-HTTP-Method-Override': 'GET'
    }
data = {
    "attrs": [ "name", "state", "last_check_result" ],
    "joins": [ "host.name", "host.state", "host.last_check_result" ],
    "filter": "match(\"ping*\", service.name)",
}

r = requests.post(request_url,
    headers=headers,
    auth=('root', 'icinga'),
    #data=json.dumps(data),
    json=data,
    verify=False)


print "Request URL: " + str(r.url)
print "Status code: " + str(r.status_code)
print "hello"
if(r.status_code == 200):
    print "Result: " + json.dumps(r.json())
else:
    print r.text
    r.raise_for_status()

