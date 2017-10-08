import requests
from pprint import pprint

port = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", 
	params={'positions' : 'BLK~25|AAPL~25|IXN~25|MALOX~25', 'currency': 'USD', 'calculateRisk': 'true', 'allDataReturned': 'false'})
# portfolioAnalysisRequest.text # get in text string format
# portfolioAnalysisRequest.json # get as json object
# pprint(port.json())

import json
with open('data.json', 'w') as outfile:
    json.dump(port.json(), outfile)