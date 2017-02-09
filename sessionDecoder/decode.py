import sys, base64

if not len(sys.argv) == 2:
	quit()

cookie = sys.argv[1]
cookie = cookie.split('.')[0] + '==='
dataStr = base64.urlsafe_b64decode(cookie)

print dataStr
