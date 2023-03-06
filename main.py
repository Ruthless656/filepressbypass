import requests
link = "https://filepress.click/file/63f2e597afbf1cfbc29cddd2"
def filepress(url):
  code = url.split("/")[-1]
  headers = {
    'authority': 'api.filepress.click',
    'origin': 'https://filepress.click',
    'referer': 'https://filepress.click/',
  }
  json_data = {
    'id': code,
    'method': 'publicDownlaod',
  }
  r = requests.post('https://api.filepress.click/api/file/downlaod/',headers=headers, json=json_data)
  data = r.json()['data']
  drive_url = ("https://drive.google.com/file/d/{link}/view".format(link=data))
  try:
        return drive_url
  except: return "Something went wrong"
  
print(filepress(link))
