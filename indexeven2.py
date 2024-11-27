#wpt print index position of even digits present in even index position in a str.
s='abi1234'
for ip in range(0,len(s),2):
    if s[ip].isdigit() and int(s[ip])%2==0 :
        print(ip)

'''
iterations...
1.get the string as a input .
2.using for loop to extract each and every elements index position in even.
     #1 s[0]='a' is not a digit than condition fails.
             increment by 2
     #2 s[2]='i' is not a digit than condition fails.
             increment by 2
     #5 s[4]='2' is digit and int(2) is even and ,enter if block and print 4.
             increment by 2
     #7 s[6]='4' is digit and int(6) is even and ,enter if block and print 6.

'''