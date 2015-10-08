import redis

__author__ = 'bernie'

r = redis.StrictRedis(host='localhost', port=6379, db=0)
name = r.get('name')
print name
