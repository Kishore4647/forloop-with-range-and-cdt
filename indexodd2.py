#wpt print even digits present in odd index position.
s='a1b2i34'
for ip in range(1,len(s),2):
    if s[ip].isdigit() and int(s[ip])%2==0:
        print(s[ip])