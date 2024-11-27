#reverse a given str without using slicing.
s='kishore'
new=''
for ip in range(-1,-(len(s)+1),-1):
    new+=s[ip]
print(new)

"""s=input()
rev=''
for i in s:
    rev=i+rev
print(rev)"""

'''
iterations...
1.get the string as the input from the user
2.create empty string .
3.using for loop with range of -1 to -(len('kishore')+1) and updation will be -1.
  #1 it will ip=-1 and add s[-1]='e' to empty string. new='e'
  #2 it will ip=-2 and add s[-2]='r' to empty string. new='er'
  #3 it will ip=-3 and add s[-3]='o' to empty string. new='ero'
  #4 it will ip=-4 and add s[-4]='h' to empty string. new='eroh'
  #5 it will ip=-5 and add s[-5]='s' to empty string. new='erohs'
  #6 it will ip=-6 and add s[-6]='i' to empty string. new='erohsi'
  #7 it will ip=-7 and add s[-7]='k' to empty string. new='erohsik'
o\p='erohsik'
'''