
import requests, json
from datetime import date, timedelta

#authorize
url = 'https://api.sumup.com/authorize'
body = ''
response = requests.get(
        url,
        body, headers={'response_type': 'code',
                       'redirect_uri': 'https://me.sumup.com/callback',
                       'client_id': '5UxmEj--5f6DS-rQzPmn2hfMweDo',
                       'scope': 'payments transaction.history user.profile user.app-settings payment_instruments',
                       'state': '2cFCsY36y95lFHk4'
              }
        )
print (response)

#get bearer token
url = 'https://api.sumup.com/token'
body = ''
response = requests.post(
        url,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        data={'grant_type': 'password',
              'client_id': '5UxmEj--5f6DS-rQzPmn2hfMweDo',
              'username': 'simonballepsa@gmail.com',
              'password': 'E8us[>m\";fy%\\UT]'
              }
        )

if(response.ok):
	# Loading the response data into a dict variable 
	# json.loads takes in only binary or string variables so using content to fetch binary content 
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON) 
    jData = json.loads(response.content)
    #print(jData)
    print("The response contains {0} properties".format(jData)) 
    print("\n") 
    for key in jData: 
        print (key + " : " + str(jData[key]))
    #store token
    access_token = jData['access_token']     
else: 
    # If response code is not ok (200), print the resulting http error code with description 
    print("Failure")
    response.raise_for_status()

print(access_token)

#list transactions and get ids
today = date.today()
day = today - timedelta(days=7)
iso = day.isoformat()

requests.packages.urllib3.disable_warnings()  

url = 'https://api.sumup.com/v0.1/me/transactions/history'
response = requests.get(
        url,
        headers={'Content-Type': 'application/json',
                 'Authorization': 'Bearer ' + access_token
                },
        params={'changes_since': iso,
              'limit': '10'
        }
        )

if(response.ok):
	# Loading the response data into a dict variable 
	# json.loads takes in only binary or string variables so using content to fetch binary content 
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON) 
    jData = json.loads(response.content)
    print(jData)
    #print("The response contains {0} properties".format(jData)) 
    #print("\n") 
    #for key in jData: 
        #if key == 'amount':
       # print (key + " : " + str(jData[key]) + "\n")
    #print (jData['items'][0]['amount'])

    for item in jData['items']:
        print(item['transaction_code'])
        print(item['amount'])

    #for idx in jData['items']:
        #print (idx)
     #   print ()

    #print jData['items']['id]']

    #store token
    #access_token = jData['access_token']    
        #print (jData['timestamp'])
        #print (jData['amount'])
        #print (jData['/n'])    
    #  
else: 
    # If response code is not ok (200), print the resulting http error code with description 
    print("Failure")
    response.raise_for_status()

#print(access_token)

#get transactions
today = date.today()
day = today - timedelta(days=7)
iso = day.isoformat()

requests.packages.urllib3.disable_warnings()  

url = 'https://api.sumup.com/v0.1/me/transactions'
response = requests.get(
        url,
        headers={'Content-Type': 'application/json',
                 'Authorization': 'Bearer ' + access_token
                },
        params={'transaction_code': 'TD63RA477P'
        }
        )

if(response.ok):
	# Loading the response data into a dict variable 
	# json.loads takes in only binary or string variables so using content to fetch binary content 
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON) 
    jData = json.loads(response.content)
    print(jData)
    #print("The response contains {0} properties".format(jData)) 
    #print("\n") 
    #for key in jData: 
        #if key == 'amount':
       # print (key + " : " + str(jData[key]) + "\n")
    #print (jData['items'][0]['amount'])

    #for item in jData['items']:
    #    print(item['transaction_code'])
    #    print(item['amount'])

    #for idx in jData['items']:
        #print (idx)
     #   print ()

    #print jData['items']['id]']

    #store token
    #access_token = jData['access_token']    
        #print (jData['timestamp'])
        #print (jData['amount'])
        #print (jData['/n'])    
    #  
else: 
    # If response code is not ok (200), print the resulting http error code with description 
    print("Failure")
    response.raise_for_status()

#print(access_token)


#dcc9b0d6-874b-4cb4-9441-3fff868ac5ca

#get products from transaction id

requests.packages.urllib3.disable_warnings()  

url = 'https://api.sumup.com/v1.0/receipts/TD63RA477P'
response = requests.get(
        url,
        headers={'Content-Type': 'application/json',
                 'Authorization': 'Bearer ' + access_token,
                },
        params={'mid': 'M9KS4HS4'
        }
        )

if(response.ok):
	# Loading the response data into a dict variable 
	# json.loads takes in only binary or string variables so using content to fetch binary content 
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON) 
    jData = json.loads(response.content)
    print(jData)
    #print("The response contains {0} properties".format(jData)) 
    #print("\n") 
    #for key in jData: 
        #if key == 'amount':
       # print (key + " : " + str(jData[key]) + "\n")
    #print (jData['items'][0]['amount'])

    #for item in jData['items']:
    #    print(item['id'])

    #for idx in jData['items']:
        #print (idx)
     #   print ()

    #print jData['items']['id]']

    #store token
    #access_token = jData['access_token']    
        #print (jData['timestamp'])
        #print (jData['amount'])
        #print (jData['/n'])    
    #  
else: 
    # If response code is not ok (200), print the resulting http error code with description 
    print("Failure")
    response.raise_for_status()

requests.packages.urllib3.disable_warnings()  

url = 'https://me.sumup.com/en-gb/reports/online-store'
response = requests.get(
        url,
        headers={'Content-Type': 'application/json',
                 'Authorization': 'Bearer ' + access_token,
                },
        )

if(response.ok):
	# Loading the response data into a dict variable 
	# json.loads takes in only binary or string variables so using content to fetch binary content 
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON) 
    jData = json.loads(response.content)
    print(jData)
    #print("The response contains {0} properties".format(jData)) 
    #print("\n") 
    #for key in jData: 
        #if key == 'amount':
       # print (key + " : " + str(jData[key]) + "\n")
    #print (jData['items'][0]['amount'])

    #for item in jData['items']:
    #    print(item['id'])

    #for idx in jData['items']:
        #print (idx)
     #   print ()

    #print jData['items']['id]']

    #store token
    #access_token = jData['access_token']    
        #print (jData['timestamp'])
        #print (jData['amount'])
        #print (jData['/n'])    
    #  
else: 
    # If response code is not ok (200), print the resulting http error code with description 
    print("Failure")
    response.raise_for_status()







