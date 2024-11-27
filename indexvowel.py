#wpt print the index position of vowels in given str.
s = 'kishore'
s = s.lower()
v='aeiou'
for ip in range(len(s)):
    if s[ip] in v:
        print(ip)

'''
iterations...
1.getting str 'kishore' as input from the user.
2.converting the str into lowercase.
3.define vowels in variable v.
4.using for loop with range and cdt to iterate the string element and index.
    1.s[ip] = 'k' and check its in v 
'''