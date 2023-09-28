# get request to ipfs to first load each json data entry at least once
# post request to joepegs refresh metadata

import requests
import time

# Parameters here
collectionSize = [SIZE] # int e.g. 10000
ipfsImageLocation = '[LOCATION]' # string e.g. 'https://bafybeifmbd3snpo2xxx422xexo2oeqibi4m4heh67va2ejsdps5atez5xi.ipfs.dweb.link/'
collectionAddr = '[CONTRACT ADDRESS]' # string e.g. '0xa8f5767fxxx765742ed55ca7e04ecf880f745c4e'

def startRequests(_collectionSize, _ipfsImageLocation, _collectionAddr):
  for i in range(0, _collectionSize):
    
    print('ID: ' + str(i) + 'in process..........')

    a = requests.get(_ipfsImageLocation + '%d' % i)
    print(a.status_code)
    print(a.content)
    
    r = requests.post('https://barn.joepegs.com/v2/items/refresh-metadata', json={
        'collection': _collectionAddr,
        'tokenId': "%d" % i
    })

    print(r.status_code)
    print(r.json())

    time.sleep(5) #Adjustable to avoid request gateway time-out

startRequests(collectionSize, ipfsImageLocation, collectionAddr)