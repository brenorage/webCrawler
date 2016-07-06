import requests
def makeRequest(url):
    r = requests.get(url)
    statusCode = r.status_code
    print(statusCode)
    if statusCode == 200 :
        print(r.text)
    else :
        print('Problema na conexão')
