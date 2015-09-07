import hashlib

__author__ = 'bida'


s = '20150702094126220936671706069DDClick521'
m = hashlib.md5()
m.update(s)
print m.digest()
print m.hexdigest()
