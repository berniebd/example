# -*- encoding:utf-8 -*-
from Crypto import Random
from Crypto.PublicKey import RSA

__auth__ = 'bida'

if __name__ == '__main__':
    from Crypto import Random
    from Crypto.PublicKey import RSA
    random_generator = Random.new().read
    rsa = RSA.generate(2014, random_generator)
    private_key = rsa.exportKey()
    public_key = rsa.publickey().exportKey()