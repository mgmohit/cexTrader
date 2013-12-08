import cexapi

configFile = open('cex.config', 'r')

line = configFile.readline()

config = line.split(":")

username = config[1]
api_key = config[3]
api_secret = config[5]

print username
print api_key
print api_secret

api = cexapi.api(username,api_key,api_secret)

ticker = api.ticker('GHS/BTC')
balance = api.balance()

print ticker
print api.balance()

ticker.items()
balance.items()
btc = balance['BTC']
ghs = balance['GHS']
btc.items()
ghs.items()

print "Last Price (btc/ghs): %s" % ticker['last']

print "Available btc balance: %s" % btc['available']
print "Current GHS: %s" % ghs['available']

#api.place_order('buy', 0.00001, ticker['last'], 'GHS/BTC')

