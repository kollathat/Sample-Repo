with open('test.txt', 'w') as write_file:
    write_file.write("Hello, I'm a file!")

with open('test.txt', 'r') as read_file:
    print(read_file.read())

with open('test.txt', 'a') as write_file:
    write_file.write("\nHere's some more text.")

with open('test.txt', 'r') as read_file:
    print(read_file.read())

with open('test.txt', 'w') as write_file:
    write_file.write("All the text has been deleted!")

with open('test.txt', 'r') as read_file:
    print(read_file.read())

write_file = open('test.txt', 'w')
write_file.write("Original text")

write_file.close()