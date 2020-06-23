import requests
import time
from webhooktest.models import Transaction

import requests
import time
import os
import requests
import time

response = requests.get('https://blockchain.info/latestblock')
hash = response.json()['hash']
while True:
    if hash != response.json()['hash']:
        newhash = response.json()['hash']
        try:
            oldresp = response
            response = requests.get(
                f'https://blockchain.info/rawblock/{newhash}')
            print("we find a new hash!!!!")
            hash = newhash
            print(newhash)
            for transaction in response.json()['tx']:
                for output in transaction['out']:
                    transaction = Transaction(
                        address=output['addr'],
                        amount=output['value'])
                    transaction.save()
            response = requests.get('https://blockchain.info/latestblock')
        except:

            print("we failed to load raw block")
            response= oldresp
            continue
    elif hash == response.json()['hash']:
        try:
            response = requests.get('https://blockchain.info/latestblock')
        except:
            print("failed to do shit!!!")
            continue
# , CryptoHook
# # Create your tests here.
from django.contrib.auth.models import User
from rest_hooks.models import Hook

# jrrtolkien = User.objects.create(username='jrrtoasdfabfacq')
#

