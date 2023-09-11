##
## Introduction to accessing API's in the internet using python
## For more information about other publically available and free
## API's please check the following link:
##
## - https://github.com/public-apis/public-apis
##
## for more information about using and creating API's
## with python check out this site:
## - https://realpython.com/api-integration-in-python/
##
import requests
import json

## in this simple API query program we're going to pull down factual information
## about cats. The base URL is shown in "catFactURL" while the actual
## API endpoint we're going after is assigned to "catFactQuery"
##
## The query itself is asking for 2 random facts about cats
##
catFactURL = "https://cat-fact.herokuapp.com"
catFactQuery = "/facts/random?animal_type=cat&amount=2"

## we concatenate the two variables shown above to construct the
## complete query string for the API call
##
catFactURL_and_Query = catFactURL + catFactQuery

## invoke the API using the requests.get method, we'll pass in the
## URL/Query string we created above and get the response from
## our API query in "catFactResponse"
##
catFactResponse = requests.get(catFactURL_and_Query)

## if we get anything other than a "200" as the response code then
## something has gone wrong with our api query. Print out the status
## code if it's NOT 200
##
if catFactResponse.status_code != 200:
    raise APIError('GET /facts/random?animal_type=cat&amount=2 {}'.format(cactFactResponse.status_code))

## Print some type of heading to clearly show the information we're
## printing below. Dump the raw JSON response, prettified that is so
## it's easier to read than the raw json
##
print ("\n\n----------------------------------")
print ("Here is the original response from the API call in JSON format...")
print (json.dumps(catFactResponse.json(), indent=1))

## print another header to clearly seperate the next printout from the
## json dump just above
## We're going to loop through the block of json we got back as a response
## print print out just the fact ID and the fact text
##
print ("\n\n----------------------------------")
print ("Here are just the ID and text of the responses")
for factItem in catFactResponse.json():
    print ('{} {}'.format(factItem['_id'], factItem['text']))
