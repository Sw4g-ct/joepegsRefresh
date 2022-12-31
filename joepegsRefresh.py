# get request to ipfs to first load each json data entry at least once
# post request to joepegs refresh metadata

import requests
import time

def startRequests():
  for i in range(80, 90):
    
    print('ID: ' + str(i) + 'in process..........')

    a = requests.get('https://bafybeifmbd3snpo2ye3422xexo2oeqibi4m4heh67va2ejsdps5atez5xi.ipfs.dweb.link/%d' % i)
    print(a.status_code)
    print(a.content)
    
    r = requests.post('https://barn.joepegs.com/v2/items/refresh-metadata', json={
        "collection": "0xa8f5767f78c765742ed55ca7e04ecf880f745c4e",
        "tokenId": "%d" % i
    })

    print(r.status_code)
    print(r.json())

    time.sleep(5)

startRequests()