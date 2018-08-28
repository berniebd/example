# -*- coding: utf-8 -*-
# Created by bida on 2018/8/2

class Synthesizer(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'

class Human(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'

class Computer(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'execute a program'

class Adapter(object):
    def __init__(self, obj, adapted_method):
        self.obj = obj
        self.__dict__.update(obj.__dict__)
        self.__dict__.update(adapted_method)

    def __str__(self):
        return str(self.obj)

if __name__ == '__main__':
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print('{}, {}'.format(str(i), i.execute()))
        print(i.name)
