file = open("my_file.txt", )
content = file.read()
print (content)
file.close() #it is important to close a file to free up computer resources

#===== Opening a file using the With key word
#=== using the with key word eliminates the need to close the file
#=== once a read operation is complete.
with open("my_file.txt", mode = "a+") as fuk:
    fuk.write("new text\n")
    content = fuk.read()
    print(content)