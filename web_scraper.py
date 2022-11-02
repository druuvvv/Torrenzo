import requests 
import time
def torrent(request_name):
  URL = f'http://tuna.anu.ninja:9117/api/v2.0/indexers/all/results?apikey=v006hqe1v7o2snicw4ruvffbyymaxbxr{request_name}'
  response = requests.get(URL)  
  dictionary = response.json()
  links = {'Title' : [] , 'LINK' : [] , 'Seeders' : [] , 'Size' : [] }
  for i in range(5):
    links['Size'].append(dictionary['Results'][i]['Size'])
    links['Seeders'].append(dictionary['Results'][i]['Seeders'])
    links['Title'].append(dictionary['Results'][i]['Title'])
    try:
     links['LINK'].append(dictionary['Results'][i]['MagnetUri'])
    except:
     links['LINK'].append(dictionary['Results'][i]['Guid'])
    


  answer= links
  return answer


