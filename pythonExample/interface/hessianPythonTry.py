from pyhessian.client import HessianProxy

__author__ = 'bida'

service = HessianProxy('http://localhost:8080/HessianService')

print service.sayHello()
# List
print service.myLoveFruit()
# Dict
print type(service.myBabays())
print service.myBabays()
print service.myBabays()['daughter']
# Object,Java class
print service.getMyCar().carName
print service.getMyCar().carModel