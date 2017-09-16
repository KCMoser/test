# Playing with files
f = open('test.txt','r+')     # the r+ is read/write mode
print 'Output of read'
print f.read()
print
print 'Output of readlines'
f.seek(0)               #without this, output of readlines is empty
print f.readlines()     # returns each line as a list item
print
print 'iterating through file with for loop'
for stuff in open('test.txt'):
    print stuff
print
for i in range(2):                              # Iterate through writing lines
    f.write("This is line %s\n" % (i+1))
f.close()
f = open('test.txt')
print f.read()
f.close()