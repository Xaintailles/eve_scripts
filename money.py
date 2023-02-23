# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:35:02 2023

@author: Gebruiker
"""

#FROM: https://kyria.github.io/EsiPy/examples/sso_login_esipy/

from esipy import EsiApp
from esipy import EsiClient
from esipy import EsiSecurity
import json

app = EsiApp().get_latest_swagger

with open(r'C:\Users\Gebruiker\Desktop\secrets\secrets.json') as f:
    d_secrets = json.load(f)['WALLET_APP'][0]

redirect_uri=d_secrets['Callback URL']
client_id=d_secrets['Client ID']
secret_key=d_secrets['Secret Key']
user_agent=d_secrets['User Agent'] 

# replace the redirect_uri, client_id and secret_key values
# with the values you get from the STEP 1 !
security = EsiSecurity(
    redirect_uri=redirect_uri,
    client_id=client_id,
    secret_key=secret_key,
    headers={'User-Agent': user_agent},
)

# and the client object, replace the header user agent value with something reliable !
client = EsiClient(
    retry_requests=True,
    headers={'User-Agent': 'Something CCP can use to contact you and that define your app'},
    security=security
)

# this print a URL where we can log in
print(security.get_auth_uri(state='SomeRandomGeneratedState', 
                            scopes=['esi-wallet.read_character_wallet.v1']))


tokens = security.auth('B2I29iYb5EmHSIf_g395uQ')

print(tokens)

api_info = security.verify()

# now get the wallet data
op = app.op['get_characters_character_id_wallet'](
    character_id=api_info['sub'].split(':')[-1]
)
wallet = client.request(op)

# and to see the data behind, let's print it
print(wallet.data)