#wpt replace all vowels with their index position.
s='kishore'
s=s.lower()
v="aeiou"
new_str=' '
for ip in range(len(s)):
    if s[ip] in v:
        new_str+=str(ip)
    else:
        new_str+=s[ip]
print(new_str)

'''
iterations...

1.getting str as a input from the user.
2.coverting all char into lowercase .
3.define vowels in a variable v.
4.creating a new string to store the replaced char with index position.
5.using for loop to iterate through the str.
    1.s[ip]='k' and check its in v , if it is true than add its str(ip) to new_str, else add s[ip].  
    1.s[ip]='i' and check its in v , if it is true than add its str(ip) to new_str, else add s[ip].  #replace with 1
    1.s[ip]='s' and check its in v , if it is true than add its str(ip) to new_str, else add s[ip].  
    1.s[ip]='h' and check its in v , if it is true than add its str(ip) to new_str, else add s[ip].  
    1.s[ip]='o' and check its in v , if it is true than add its str(ip) to new_str, else add s[ip].  #replace with 4
    1.s[ip]='r' and check its in v , if it is true than add its str(ip) to new_str, else add s[ip].  
    1.s[ip]='e' and check its in v , if it is true than add its str(ip) to new_str, else add s[ip].  #replace with 6

'''