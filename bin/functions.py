""" Modulo que provee funciones para obtener datos de la API de cloudfare """
import requests


## Cloudfare functions ##

def getZoneId(zoneName, authEmail, authKey):
    """Consulta el Id de una zona DNS desde la API de cloudfare
    Requiere:
        - el nombre de la zona: zoneName as str
        - el email de autenticacion de cloudfare: authEmail as str
        - el token api global de la cuenta de cloudfare: authKey as str
    Devuelve json {
        'response': response.status_code,
        'success': True si response es 200 y zoneId <> de 0,
        'zoneid': None si hay error y la Id de la zona si es correcto
        }
    """
    url = 'https://api.cloudflare.com/client/v4/zones'
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Email': authEmail,
        'X-Auth-Key': authKey
        }
    response = requests.get(url, headers=headers, timeout=30)
    if response.status_code == 200:
        zonesinfo = response.json()
        zoneId = 0
        for zoneitem in zonesinfo['result']:
            if zoneitem['name'] == zoneName:
                zoneId = zoneitem['id']
        if zoneId == 0:
            return ({
                'response': response.status_code,
                'success': False,
                'zoneid': None
            })
        else:
            return ({
                'response': response.status_code,
                'success': True,
                'zoneid': zoneId
            })
    else:
        return ({
            'response': response.status_code,
            'success': False,
            'zoneid': None
        })


def getDNSrecordIds(zoneId, DNSrecord, authEmail, authKey):
    """Consulta el ID de un registro DNS desde la API de cloudfare
    Requiere:
        - el id de la zona: zoneName as str
        - el nombre del registro DNS: DNSrecord as string
        - el email de autenticacion de cloudfare: authEmail as str
        - el token api global de la cuenta de cloudfare: authKey as str
    Devuelve json {
        
    }
    """

    # Obtenemos los registros DNS de la zona (incluidos sus IDs)
    url = 'https://api.cloudflare.com/client/v4/zones/' + zoneId + '/dns_records'
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Email': authEmail,
        'X-Auth-Key': authKey
        }
    res = requests.get(url, headers=headers, timeout=30)
    response = res.json()
    subdomainId = None
    if res.status_code != 200:
        return ({
            'response': response.status_code,
            'success': False,
            'domainid': None
        })
    for item in response['result']:
        if item['name'] == DNSrecord and item['type'] == 'A':
            subdomainId = item['id']
    if subdomainId == None:
        return ({
            'response': response.status_code,
            'success': False,
            'domainid': None
        })

    return ({
        'response': response.status_code,
        'success': True,
        'domainid': subdomainId
    })


if __name__ == "__main__":
    zone = input("Zona a buscar: ")
    dns = input("Registro DNS a buscar: ")
    email = input("Email acceso: ")
    key = input("Global APIKey de la cuenta: ")
    print(getZoneId(zone, email, key))
    print(getDNSrecordIds(zone, dns, email, key))
