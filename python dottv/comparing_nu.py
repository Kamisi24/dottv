#user input for the genre questions
mylist= [4, 3, 45, 54, 3]

#lists are the values for the movies
list1 = [32, 33, 3, 39, 9]
list2 = [5, 4, 55, 58, 5]
list3 = [44, 14, 2, 10, 23]
list4 = [12, 33, 1, 3, 35]
list5 = [13, 12, 8, 12, 11]

#which list of numbers is more similar to mylist = list2
#min(value1, key=lambda x:abs(x-mylist[0]))
# need to find smallest distance to each ans add them up and then smallest value will be ordered first , therefore best match

#this function compares the difference between input from user score to movie score and returns overall differences
def compare(a1,a2,a3,a4,a5,b1,b2,b3,b4,b5):
    comp1 = abs(a1-b1)
    comp2 = abs(a2-b2)
    comp3 = abs(a3-b3)
    comp4 = abs(a4-b4)
    comp5 = abs(a5-b5)
    return comp1+comp2+comp3+comp4+comp5

#the results for the comparisons are stored in the variables for each film
result1 = compare(mylist[0],mylist[1],mylist[2],mylist[3],mylist[4],list1[0],list1[1],list1[2],list1[3],list1[4])
result2 = compare(mylist[0],mylist[1],mylist[2],mylist[3],mylist[4],list2[0],list2[1],list2[2],list2[3],list2[4])
result3 = compare(mylist[0],mylist[1],mylist[2],mylist[3],mylist[4],list3[0],list3[1],list3[2],list3[3],list3[4])
result4 = compare(mylist[0],mylist[1],mylist[2],mylist[3],mylist[4],list4[0],list4[1],list4[2],list4[3],list4[4])
result5 = compare(mylist[0],mylist[1],mylist[2],mylist[3],mylist[4],list5[0],list5[1],list5[2],list5[3],list5[4])

#shows the order of films
results = [result1,result2,result3,result4,result5]
#movie with the lowest score value is recommended in that order
print(sorted(results))


