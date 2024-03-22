import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
#api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces"
api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
    "ietf-interfaces:interface": {
        "name": "LoopbackStudentID",
        "description": "StudentID RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.0.15.189",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}


    resp = requests.get(api_url, auth=basicauth, data=json.dumps(yangConfig),  headers=headers, verify=False)

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
    else:
        print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))


def delete():
    resp = requests.get(api_url, auth=basicauth, data=json.dumps(yangConfig),  headers=headers, verify=False)

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Cannot delete: Interface loopback' +stdid .format(resp.status_code))


def enable():
    yangConfig = <!!!REPLACEME with YANG data!!!>

    resp = requests.get(api_url, auth=basicauth, data=json.dumps(yangConfig),  headers=headers, verify=False)

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def disable():
    yangConfig = <!!!REPLACEME with YANG data!!!>

    resp = requests.get(api_url, auth=basicauth, data=json.dumps(yangConfig),  headers=headers, verify=False)

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def status():
    api_url_status = "<!!!REPLACEME with URL of RESTCONF Operational API!!!>"

    resp = requests.get(api_url, auth=basicauth, data=json.dumps(yangConfig),  headers=headers, verify=False)

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = <!!!REPLACEME!!!>
        oper_status = <!!!REPLACEME!!!>
        if admin_status == 'up' and oper_status == 'up':
            return "<!!!REPLACEME with proper message!!!>"
        elif admin_status == 'down' and oper_status == 'down':
            return "<!!!REPLACEME with proper message!!!>"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
