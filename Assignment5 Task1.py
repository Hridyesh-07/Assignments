a = input("Enter the students name: ")
List1 = ('Alice', 'Aryan', 'James')
List2 = (85, 98, 56)
dict1 = {'Alice': 85, 'Aryan': 98, 'James': 56}
if a in dict1:
    print(f"{a}'s marks: {dict1[a]}")
else:
    print("Student not found")
