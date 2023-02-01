import time
import urllib.request
import json
import numpy as np

# School list: https://www.thegradcafe.com/api/ajax.php?W=I

base_api = 'https://www.thegradcafe.com/api/results-v2.php?page={}&institution={}&program={}&degree={}'

class GC_API():

    def __init__(self) -> None:
        pass

    def get(self, institution, program, level, cutoff=1e10, verbose=True):
        print("Fetching {} {} {}".format(institution, program, level))

        n, page = 0, 0
        ret = []
        while n < cutoff:
            n += 1
            page += 1
            res = self.fetch(institution, program, level, page)
            # print(res)
            time.sleep(0.1 + np.random.random() * 0.1)
            if len(res) == 0:
                break
            if verbose:
                print(res[-1]['date_of_notification'])
            ret += res
        print("{}: {}".format(institution, len(ret)))
        return ret
        
    def fetch(self, institution, program, level, page):
        req_api = base_api.format(page, institution, program, level)
        # print(req_api)
        try:
            return json.loads(urllib.request.urlopen(req_api).read())
        except:
            print('Failed requesting {}'.format(req_api))
            return -1