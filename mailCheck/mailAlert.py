import requests, json
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


msg = MIMEMultipart()
msg['From'] = 'icinga.smtp.alert@gmail.com'
msg['TO'] = 'icinga.smtp.alert@gmail.com'
msg['SUbject'] = 'Just smth'


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
    
    message = json.dumps(r.json())
    print "Result: " + message
    print
    message = json.loads(message)
    json_result = message["results"][0]["type"]
    print "My valluee" +  str(json_result)
    msg.attach(MIMEText(json_result))

    print 'Connecting to SMTP serveri...'
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(msg['From'],'AZqswx1234')
    print 'Sending email...'
    mailserver.sendmail(msg['From'],msg['To'],msg.as_string())
    mailserver.quit()


else:
    print r.text
    r.raise_for_status()



