<<<<<<< HEAD
try:
    file1 = open('sample.txt','r')
    reading_file1= file1.read()
    print(reading_file1)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' not found.")
=======
try:
    file1 = open('sample.txt','r')
    reading_file1= file1.read()
    print(reading_file1)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' not found.")
>>>>>>> 5064f5605eed626cae472e96d23d5c707c24d045
