#Program to define an OrderedDictionary class and some client code

class OrderedDictionary:
    ''' Class holding a dictionary with the properties:
1.	The keys of the dictionary have to be strings
2.	When items are added to the dictionary, their order of insertion is remembered and when an iterator is created to iterate over the items, it should iterate in the same order as the keys were added.
3.	Updating the value for a key doesn’t change its order, however removing and adding back a key changes its order (on insertion it will be added at the end)
4.	If the dictionary is indexed using an integer, it is treated as the index of the key insertion. So myOrderedDictionary[0] will give the value for the oldest key, myOrderedDictionary[1] will give value for the second oldest key inserted, etc.
'''
    pass

def main():
    sep = "-"*50
    d = OrderedDictionary()
##    #Add three key-value pairs
##    d['a'] = 1
##    d['b'] = 2
##    d['c'] = 3
##    d['d'] = 4
##
##    print("len(d):", len(d))
##    print('d[1]: ', d[1]) # Should print 2
##
##    #Update value for key 'b'
##    print("Updating d['b'] = 8...")
##    d['b'] = 8
##    print('d[1]: ', d[1]) # Should print 8
##    print(sep)
##    print("updating with integer index d[0] = 0. Should update d['a']")
##    d[0] = 0 # update using integer index. Should update d['a']
##    print("d['a']: ", d['a']) # Should print 0
##    print(sep)
##    #iterate using __iter__ method
##    print("Iterating ...")
##    for m in d:
##        print(m, end=",")
##    print("\n"+sep)
##
##    #iterate using keys() method
##    print("Iterating using keys()...")
##    for m in d.keys():
##        print(m, end=",")
##    print("\n"+sep)
##
##    #removing 'b'
##    print("Removing 'b'...pop('b')")
##    print(d.pop('b')) #should print 8
##    print(sep)
##    #iterate using values() method
##    print("Iterating using values()...")
##    for m in d.values():
##        print(m, end=",")
##    print("\n"+sep)
##    
##    #adding 'b' again
##    print("adding 'b' again d['b'] = 10")
##    d['b'] = 10
##    print(sep)    
##    #removing 'd'
##    print("Removing key 'd'...pop(2)")
##    print(d.pop(2)) #should print 4
##    print(sep)
##    #iterate using items() method
##    print("Iterating using items()...")
##    for m in d.items():
##        print(m, end=",")
##    print("\n"+sep)
##    
##    try:
##        print("Trying d[3.0] = 5...")
##        d[3.0] = 5 # should raise ValueError
##    except Exception as e:
##        print(e)
##    print(sep)
##    try:
##        print("Trying d[5]....")
##        print(d[5]) # should raise IndexError
##    except Exception as e:
##        print(e)
##    print(sep)
##    try:
##        print("Trying pop[3.1412]....")
##        print(d.pop(3.1412)) # should raise ValueError
##    except Exception as e:
##        print(e)
##    print(sep)    
if __name__ == "__main__":
    main()

    
