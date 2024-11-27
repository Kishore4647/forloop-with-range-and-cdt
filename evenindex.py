#wpt print element which are in even index position  in a str.
s='hai python'
for ip in range(len(s)):
    if ip%2==0:
        print(s[ip])

'''  
iterations....

1.getting str as input from the user.
2.using for to iterate the given string.
    1.ip = o in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 1 in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 2 in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 3 in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 4 in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 5 in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 6 in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 7 in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 8 in len(s), it check ip is even or not, if true print that element(s[ip]).
    1.ip = 9 in len(s), it check ip is even or not, if true print that element(s[ip]).
3.the loop will end bcoz that range is till 10.
'''