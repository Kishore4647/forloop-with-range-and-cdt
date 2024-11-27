#wpt print the students who are score above the average.
d={'amit':90,'sakthi':89,'alex':79,'adam':63,'sri':83}
new_dict={} #using new_dict so no need to modify the existing dict.
avg=0
tot=0
for i in d:      #for loop to get average score in dict
    tot+=d[i]
avg=tot/len(d)
print(f'average score of all student is {avg}')

for j in d:   #for loop for to get key and value which is >= avg score
    if d[j] >= avg:
        new_dict.update({j:d[j]})
    
print(new_dict)
