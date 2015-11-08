#coding:utf-8
from itsdangerous import Signer
s = Signer('secret')
s.sign('String'.encode())
print ('s:',s)

s.unsign('String.%s' %s)