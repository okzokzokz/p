import requests
import random
import string
import itertools
from itertools import permutations
from itertools import product


count = 776520240


results = random.sample(list(itertools.product(string.ascii_uppercase + string.ascii_lowercase + string.digits, repeat=5)), count)

for results in results:
    num = "".join(results)

r = ('https://soundcloud.com/lil_peep/nuthing-to-lose-lil-peep-x-omen-prod-purpdogg/s-'+num)
response = requests.get('https://soundcloud.com/lil_peep/nuthing-to-lose-lil-peep-x-omen-prod-purpdogg/s-'+num)
m = response.status_code

while(m!=a):
     print('Not found: '+m)

else:
     print('Found:  '+r)

    
