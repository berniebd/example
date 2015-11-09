from httmock import urlmatch, HTTMock, all_requests, response
import requests

__author__ = 'bida'

@urlmatch(netloc=r'(.*)google(.*)')
def google_mock(url, request):
    return 'feeling lucky'

@all_requests
def response_content(url, request):
    return {'status_code': 200,
            'content': 'Oh hai'}

@all_requests
def response_detail(url, request):
    headers = {'content-type': 'application/json',
               'Set-Cookie': 'foo=bar'}
    content = {'message': 'API rate limit exceeded', 'success': True}

    return response(403, content, headers, None, 5, request)

with HTTMock(google_mock):
    r = requests.get('http://www.google.com.hk')
    print r.content

with HTTMock(response_content):
    r = requests.get('http://www.baidu.com')
    print r.status_code
    print r.content

with HTTMock(response_detail):
    r = requests.get('http://www.baidu.com')
    print r.status_code
    print r.elapsed
    print r.json().get('message')
    print r.cookies['foo']