#s = input()
#print(len(s))
#print('=======',s[::-1])
#print('------------------')
#for i in range(len(s)):
#    p=s[:i]+s[i+1:]
#    print('i',i)
#    print('s[:i]',s[:i])
#    print('s[i+1:]',s[i+1:])
#    print('p',p)
#    print('p[::-1]',p[::-1])
#    print('----------------------')


s = input()
for i in range(len(s)):
    p=s[:i]+s[i+1:]
    if p==p[::-1]:
        t=True
        break
    else:
        t=False
if t:
    print('Yes')
else:
    print('No')