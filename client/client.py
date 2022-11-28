import urllib.request
fp = urllib.request.urlopen('server:3000')
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")
print(decodedContent)
fp.close()