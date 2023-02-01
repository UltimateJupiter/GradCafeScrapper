from gcapi import *
from IPython import embed
import json

from joblib import Parallel, delayed

GC = GC_API()
school_list = json.load(open('./school_list_short.json'))
programs = ['Computer_Science']
degrees = ['PhD']

log_dirc = '../meta'

def school_exec(school):
    for p in programs:
        for d in degrees:
            res = GC.get(school, p, d, verbose=False)
            # print(res)
            log_name = '{}.{}.{}.json'.format(school, p, d)
            json.dump(res, open('{}/{}'.format(log_dirc, log_name), 'w'))

Parallel(n_jobs=16)(delayed(school_exec)(s) for s in school_list)