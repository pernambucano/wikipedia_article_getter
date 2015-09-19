# link to json wikipedia list : https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&generator=search&gsrsearch=Food
# link to json extract data: /w/api.php?action=query&prop=extracts&format=json&explaintext=&exsectionformat=plain&titles=Association%20football

import schedule
import time
import json
import urllib
import sys

def saveFile(text, title):
    file = open("files/"+title+'.txt', 'w')

    text = title + "\n" + text

    file.write(text.encode('utf8'))
    file.close()


# get the text from the wikipedia page
def getExtractJson(page_id):
    mUrl = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&explaintext=&exsectionformat=plain&pageids="

    call_to_wikipedia = urllib.urlopen(mUrl + page_id)
    response = call_to_wikipedia.read()
    call_to_wikipedia.close()

    parsed_response = json.loads(response)

    title = parsed_response['query']['pages'][page_id]['title']
    extract = parsed_response['query']['pages'][page_id]['extract']

    #create file
    saveFile(extract, title)

# get the list of titles
def getListOfTitles():
    mUrl ="https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&generator=search&gsrsearch=Nutrition&gsrlimit=50"

    call_to_wikipedia = urllib.urlopen(mUrl)
    response = call_to_wikipedia.read()
    call_to_wikipedia.close()
    # print(response)

    parsed_response = json.loads(response)
    # print(parsed_response)
    # print(parsed_response['query']['pages'])

    for page in parsed_response['query']['pages']:
        # print page['title']
        # here we have the pages titles through page['title']
        getExtractJson(page)



if __name__ == '__main__':
    getListOfTitles()
