# -*- encoding:utf-8 -*-
from jinja2 import Template

__author__ = 'bida'

items = [{'a':1, 'b':2}, {'a': 11, '': 22}]

temp = '''
<ul>
{% for item in items %}
    <b>{{item.get('a')}}</b>
    <b>{{item['b']}}</b>
{% endfor %}
</ul>
'''

template = Template(temp)
print(template.render(items=items))