# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[k] for k in keylist]

def list2dict(L, keylist): return {k:L[i] for i, k in enumerate(keylist)}

def listrange2dict(L):
	return list2dict(L, [i for i in enumerate(L)])
