friends =[ "Akter", "Ashik" , "Ashik"]
numbers = [2,30,24,7,9]

print(friends[0])

friends.append("Ashique") ##to insert a string
print(friends)

friends.insert(1,"ak") ## inserting by values
print(friends)

friends.remove("ak")

print(friends)

friends.pop() ###delets last element
print(friends,"Delets last element ")

print(friends.index("Ashik"))  ###search index value

print("Counts The Number of same word : ",(friends.count("Ashik")))

numbers.sort()

print("it will print number in a sequence : ",numbers)
friends.clear() ## empty

print(friends)
