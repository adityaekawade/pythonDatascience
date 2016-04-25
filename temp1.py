

#creating a list of list
list_of_top_scores1 = [["tendulkar", 200],
                      ["sehwag", 219],
                      ["ganguly", 183],
                      ["dhoni", 183],
                      ["kohli", 183],
                      ["dravid", 153]]

print(list_of_top_scores1)
print(type(list_of_top_scores1))


#creating a list
scores = ["tendulkar", 200,"sehwag", 219,"ganguly", 183,"dhoni", 183,"kohli", 183, "dravid", 153]
print(scores)  #printing the list



print(scores[4])  #printing the element at index 4

print(scores[11]) #printing the element at index 11

print(scores[-1]) #negative index to print the last element in the list

#List Slicing:
print(scores[3:9])

print(scores[:4])

print(scores[7:])

#Changing the value at index 3
scores[3] = 319
print(scores)

#Substituting the values
scores[8:10] = "yuvraj", 139
print(scores)

#adding the elements in the list
scores[12:14] = "kohli", 183
print(scores)


