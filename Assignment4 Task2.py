<<<<<<< HEAD
user_input = input('Enter text to write to the file: ')
print('Data successfully written to output.txt')
file1 = open('output.txt', "r+")
writing_file = file1.write(user_input + '\n')
file1.close()
user_append = input('Enter additional text to append: ')
print('Data successfully appended')
file1 = open('output.txt', "a")
appending_file = file1.write(user_append)
file1.close()
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
=======
user_input = input('Enter text to write to the file: ')
print('Data successfully written to output.txt')
file1 = open('output.txt', "r+")
writing_file = file1.write(user_input + '\n')
file1.close()
user_append = input('Enter additional text to append: ')
print('Data successfully appended')
file1 = open('output.txt', "a")
appending_file = file1.write(user_append)
file1.close()
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
  print(file.read())
>>>>>>> 5064f5605eed626cae472e96d23d5c707c24d045
