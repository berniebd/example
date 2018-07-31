# -*- encoding:utf-8 -*-
import re
from collections import abc

__auth__ = 'bida'

RE_WORD = re.compile('\w+')

class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    # def __getitem__(self, index):
    #     return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence({0})'.format(self.text)

class Sentence3(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word
        return

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence({0})'.format(self.text)


if __name__ == '__main__':
    s = Sentence('"The time has come,", the Walrus said,')
    s3 = Sentence3('"The time has come,", the Walrus said,')
    # print(s)
    # for word in s:
    #     print(word)

    print(isinstance(s3, abc.Iterable))
    try:
        iter(s3)
    except:
        print('s is not an iterator')