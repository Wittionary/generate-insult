import json
import random

def lambda_handler(event, context):
    # TODO implement
    with open('library.json') as json_file:
        library = json.load(json_file)

    adjectiveLength = len(library['adjective'])
    noun1Length = len(library['noun1'])
    noun2Length = len(library['noun2'])

    insult = library['adjective'][random.randint(0, (adjectiveLength -1))] +" "+ \
        library['noun1'][random.randint(0, (noun1Length -1))] +" "+ \
        library['noun2'][random.randint(0, (noun2Length -1))]
    
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': json.dumps(insult)
    }