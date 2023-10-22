## version 0.1
## Script funcional con el dominio a actualizar insertado en el código

import requests
from configparser import ConfigParser

### Cargamos las variables del fichero config.ini
config = ConfigParser()
config.read('config.ini')

server = config.get('main','server')
lastip = config.get('main','lastip',fallback='0.0.0.0')
APItoken = config.get('cloudfare', 'token')
globalAPI = config.get('cloudfare', 'globalApi')
subdomains = config.get('domains', 'subdomains')

### Comprobamos nuestra IP publica

currentpublicip = requests.get(server).text.strip()


url = 'https://api.cloudflare.com/client/v4/zones/ece0ef24f77fa672e1d7e7f166078b26/dns_records'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + APItoken}
res = requests.get(url, headers=headers)
response = res.json()
for item in response['result']:
    if item['name'] == 'heimdall.javiescartin.es' and item['type'] == 'A':
        itemid = item['id']
        print('La zona ', item['name'], ' tiene el id: ', itemid)

if currentpublicip == lastip:
    print('la ip ' + currentpublicip + ' registrada la ultima vez, no ha cambiado')
else:
    try:
        config.set('main','lastip',currentpublicip)
        url = "https://api.cloudflare.com/client/v4/zones/ece0ef24f77fa672e1d7e7f166078b26/dns_records/" + itemid
        headers = {'Content-Type': 'application/json', 'X-Auth-Email': 'javi@javiescartin.com', 'X-Auth-Key': globalAPI}
        body = {
            'content': ip,
            'name': 'heimdall.javiescartin.es',
            'type': 'A'
        }
        print(url,headers,body)
        res = requests.put(url, headers=headers, json=body)
        print(res.content)
        with open('config.ini','w') as configfile:
            config.write(configfile)
        print('La ultima ip ' + lastip + ' ha cambiado a ' + ip)
    except:
        print('La ultima ip ' + lastip + ' ha cambiado a ' + ip + ' pero no ha podido actualizarse')

print(ip)
print(subdomains)
print(subdomains.split())
