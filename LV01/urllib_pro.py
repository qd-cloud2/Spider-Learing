import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
res = urllib.request.urlopen('https://www.httpbin.org/post', data=data, timeout=1)
"""
data参数： post请求使用
timeout参数： 超时时间
context参数： 用于ssl验证
cafile参数： 指定CA证书
capath参数： 指定CA证书路径
"""

# print(res.status)
# print(res.getheaders())
# print(res.getheader('Server'))
# print(res.read().decode('utf-8'))




# Request类
from urllib import request, parse

url = 'https://www.httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Host': 'www.httpbin.org'
}
dict = {'name': 'germey'}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url, data=data, headers=headers, method='POST')

"""
url参数： 请求地址
data参数：必须传bytes类型，数据是字典，先用urllib.parse.urlencode编码
headers参数：请求头
origin_req_host参数：请求方host或者ip地址
unverifiable参数：默认False，意思是用户没有足够权限接收请求结果
method参数：请求方法
"""
response = request.urlopen(req)
req.add_header('User-Agent', headers['User-Agent'])
print(response.read().decode('utf-8'))




# 高级用法

'''
HTTTPDef
'''
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

# 代理
from 
