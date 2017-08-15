
# Playing with files
f=open('test.txt')
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
