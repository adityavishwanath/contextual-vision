from __future__ import print_function
import sys
import os
from image_search import bing_search

sys.path.append("./alchemy_api")
os.system("python alchemy_api/alchemyapi.py d7a4b54fa1b12a95cd3cba4bbd5c922815f0e6cf")

from alchemyapi import AlchemyAPI
import json

#demo_url = 'http://www.kidsworldfun.com/shortstories_aholeinthefence.php'
demo_text = 'The quick brown fox jumped over the lazy dog.'
imagemap = {}

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response['keywords']:
        query = keyword['text'].encode('utf-8')
        imagemap[query] = bing_search(query, 'Image')
        print('text: ', query)
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response['statusInfo'])
