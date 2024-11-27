#wpt print odd num present in even index position.
s='abi4321'
for ip in range(len(s)):
    if s[ip].isdigit() and int(s[ip])%2==1 and ip%2==0:
        print(s[ip])

'''
iterations...
1.get the string as a input .
2.using for loop to extract each and every index position of a element.
     #1 s[0]='a' is not a digit than condition fails.
     #2 s[1]='b' is not a digit than condition fails.
     #3 s[2]='i' is not a digit than condition fails.
     #4 s[3]='4' is digit and int(4) is not odd so condition fails.
     #5 s[4]='3' is digit and int(3) is odd and ip=4 is even,enter if block and print 3.
     #6 s[5]='2' is digit and int(2) is not odd so condition fails.
     #7 s[4]='1' is digit and int(1) is odd and ip=4 is even,enter if block and print 3.


'''