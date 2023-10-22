import bin.functions as functions
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

server = config.get('main','server')
lastip = config.get('main','lastip',fallback='0.0.0.0')
authEmail = config.get('cloudfare', 'email')
APItoken = config.get('cloudfare', 'token')
globalAPI = config.get('cloudfare', 'globalApi')
zoneName = config.get('domains', 'domain')
subdomains = config.get('domains', 'subdomains')

subdomain = subdomains.split()[0] # Priemr dominio para pruebas

print('Consulta de Id de zona para ' + zoneName + ' con el usuario ' + authEmail + ' y apiKey correcta.')
print(functions.getZoneId(zoneName, authEmail, globalAPI))

print('Consulta de Id de dominio para ' + subdomain + ' con el usuario ' + authEmail + ' y apiKey correcta.')
print(functions.getDNSrecordIds(zoneName, subdomain, authEmail, globalAPI))

print('Consulta de Id de zona para pepe.com con el usuario ' + authEmail + ' y apiKey correcta.')
print(functions.getZoneId('pepe.com', authEmail, globalAPI))

print('Consulta de Id de dominio para subdomain.pepe.com con el usuario ' + authEmail + ' y apiKey correcta.')
print(functions.getDNSrecordIds('pepe.com', 'subdomain.pepe.com', authEmail, globalAPI))

print('Consulta de Id de zona para ' + zoneName + ' con el usuario ' + authEmail + ' y apiKey correcta.')
print(functions.getZoneId(zoneName, authEmail, globalAPI))

print('Consulta de Id de dominio para fake.javiescartin.es con el usuario ' + authEmail + ' y apiKey correcta.')
print(functions.getDNSrecordIds(zoneName, 'fake.javiescartin.es', authEmail, globalAPI))
