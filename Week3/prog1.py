# Difference between r+ and w+

# Reading with r+
# It simply reads the content of the file
# And file should exist else it will show an error
with open("text.txt", "r+") as f:
    print("Reading in r+")
    print(f.read())

# Reading with w+
# It will override the contents of the file
# Erases the content of the file
# Will create a file if not present
with open("text.txt", "w+") as files:
    print("Reading in w+")
    files.seek(0)
    print(files.read())

# Writing in r+
# Overriding the content of the file
with open("text.txt", "r+") as fd:
    print("Writing in r+")
    fd.write("New text 3")
    fd.seek(0)
    print(fd.read())

# Writing the content using w+
# Overrides the content written in the file
with open("sample.txt", "w+") as fd:
    print("Writing in w+")
    fd.write("New text 2")
    fd.seek(0)
    print(fd.read())

# with open('a.txt', 'r+')as fd:
   # pass # Since file does not exist, THIS will show an ERROR

# Will not show any error
with open("b.txt", "w+") as fd:
    pass
