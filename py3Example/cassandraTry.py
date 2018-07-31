# -*- encoding:utf-8 -*-
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

__auth__ = 'bida'

if __name__ == '__main__':
    auth_provider = PlainTextAuthProvider(username='hduser03', password='hduser03')
    cluster = Cluster(['10.118.80.144'], auth_provider=auth_provider)
    session = cluster.connect('ubiowner')
    rows = session.execute("select start_fee from ubi_policy_info where vin = 'LSJA0000000000565'")
    for row in rows:
        print(row[0])