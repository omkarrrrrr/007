import urllib.request

webUrl = urllib.request.urlopen('https://www.youtube.com/user/guru99com')

print("result code: "+str(webUrl.getcode()))

data = webUrl.read()
print(data)
