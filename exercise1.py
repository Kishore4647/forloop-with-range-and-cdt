#input => l=[11,22,33,44,-1,66,50] o/p > ['odd','even','odd','even',-1,'even','even']
l=[11,22,33,44,-1,66,50]
for ip in range(len(l)):
    if l[ip]%2==0 and l[ip]>0:
        l[ip]='even'
    elif l[ip]%2==1 and l[ip]>0:
        l[ip]='odd'
    else:
        l[ip]=l[ip]
print(l)

'''
->print 'odd' if the element is odd  and 
print 'even' if the element is even  and 
if the given number is negative the print that element as it is.<-
iterations,,,
1.getting the list of numbers as a input
2.using for loop get the ip,
3.using if-elif statement to check odd or even or negative,
   #l[0] is 11 is odd and greater than 0 , so l[0]='odd'.
   #l[1] is 22 is even and greater than 0 , so l[1]='even'.
   #l[2] is 33 is odd and greater than 0 , so l[2]='odd'.
   #l[3] is 44 is even and greater than 0 , so l[3]='even'.
   #l[4] is -1 is negativve and less than 0 , so l[-1]=-1
   #l[5] is 66 is even and greater than 0 , so l[1]='even'.
   #l[6] is 50 is even and greater than 0 , so l[1]='even'.

'''