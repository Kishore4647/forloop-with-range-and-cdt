#wptp print odd num present in the odd index position.
s='abi1234'
for ip in range(len(s)):
    if s[ip].isdigit() and  int(s[ip])%2==1:
        if ip%2==1:
            print(s[ip])
            