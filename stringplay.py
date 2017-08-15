s="Hello"
print s[:4]
print s.upper()
s="Goodbye"
print s
print s[4:]
s='Third change of string'
print s.upper()
a = s[::-1]                 #bracketed code reverses a string
print a
print 'Test this out: %s' %(s)
print 'Test this out: %s' %(a) 
print 'Test this out: %s' %('This is stuff')
print
print
# Now on to Lists
mylist = ['item 1',2,'item 3']
print mylist
print mylist[0]
b='something to add'
mylist.append(b)
print mylist
mylist.pop(0)             #pop is the remove command for lists
print mylist
print mylist.pop(0)       #removed first item from list and printed first item
print mylist
l2 = [1,2,3]
l3 = [7,8,9]
mylist = ['four', 'five', 'six']
matrix = [l2, mylist, l3]
print matrix
print matrix [1]
print matrix [1][1]
matrix[1].pop(2)        #removes element 2 from list 1 in matrix
print matrix
print
print
# Now dictionaries
md ={'key1':'first value','key2':'second key value','key3':100}
print md
print md['key2']
print md['key2'][11:]       # finds just word value in second key
md['key3'] += 100
print md['key3']
md['key4']=125              # adds key and value to dictionary
print md
md['key4'] -=25             # creates new key and value in dictionary
print md
d={'k1':[1,2,3]}
print d['k1'][1]
print
print