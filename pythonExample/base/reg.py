import simplejson

__author__ = 'bida'

# import re
# pattern = re.compile(r'setTimeVal\(\"(\d+)\", \"(\d+)\"\);setURL')
#
# print pattern
# res = pattern.search('setTimeVal("1435632246418", "357607616");setURL').groups()
# print len(res)
# print res[0]
# print res[1]

str = 'jsonp1435637609034({"check_person":"true","person_repid":"nxuk99mFpcDYAzSo9kR\/UvoCppCV3vGvdUm9S53It3SIK048XO8EdWwb9aYt6Sd91GBoHWIdp4Mc38tDNXsOMcaTAPUymIakGEEEVCGNzfV0WQY2l5ngO\/jEWwrhrL0M\/odYvyYjix4KOBs0Vx+mxjTkKoSnM7D5WeSNp2qra0aMLuP2Z1UaPw==","error_msg":"normal","sa_level":"0","view":"CYWaGr0EQG4="})'
print str[19:-1]
dict = simplejson.loads(str[19:-1])
print dict