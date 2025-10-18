# ----------------------------------------------------------------------------
# Name: Richard Veloz Salazar
# Class: Data Structures and Algorithms in Python
# Date: October 15, 2025
# Assignment: OrderedDictionary Implementation
#
#
# Description:
# This program implements a custom OrderedDictionary class that maintains
# key-value pairs in insertion order while allowing both string and integer
# indexing. The class ensures keys are strings, preserves insertion order 
# even when items are updated, and provides methods for safe access,
# iteration, and modification without altering order unintentionally.
# ----------------------------------------------------------------------------
#
#Program to define an OrderedDictionary class and some client code

class OrderedDictionary:
    ''' Class holding a dictionary with the properties:
1.	The keys of the dictionary have to be strings
2.	When items are added to the dictionary, their order of insertion is remembered and when an iterator is created to iterate over the items, it should iterate in the same order as the keys were added.
3.	Updating the value for a key doesn’t change its order, however removing and adding back a key changes its order (on insertion it will be added at the end)
4.	If the dictionary is indexed using an integer, it is treated as the index of the key insertion. So myOrderedDictionary[0] will give the value for the oldest key, myOrderedDictionary[1] will give value for the second oldest key inserted, etc.
'''
    def __init__(self):
        self.__dictionary = {}
        self.__listOfkeys = []
    
    # Internal helper to validate index
    def __validate_index(self, index):
        if not isinstance(index, (str, int)):
            raise ValueError(f"Index must be a string or an integer, got {type(index).__name__}")
    
    # Convert integer index to key
    def __key_from_index(self, index):
        if isinstance(index, int):
            if index < 0 or index >= len(self.__listOfkeys):
                raise IndexError("Integer index out of range")
            return self.__listOfkeys[index]
        return index # if string, it is already a key. 
    
    # Get item
    def __getitem__(self, index):
        self.__validate_index(index)
        key = self.__key_from_index(index)
        return self.__dictionary[key]
    
    # Set item
    def __setitem__(self, index, value):
        self.__validate_index(index)
        if isinstance(index, str):
            key = index
        else:
            key = self.__key_from_index(index)
        
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        
        # If key exists, update value without changing order
        if key in self.__dictionary:
            self.__dictionary[key] = value
        else:
            # New key: add at end
            self.__dictionary[key] = value
            self.__listOfkeys.append(key)

    # Get lenght 
    def __len__(self):
        return len(self.__listOfkeys)
    
    # Iterator (over keys)
    def __iter__(self):
        for key in  self.__listOfkeys:
            yield key
    
    # pop by key or index
    def pop(self, index):
        self.__validate_index(index)
        key = self.__key_from_index(index)
        value = self.__dictionary.pop(key)
        self.__listOfkeys.remove(key)
        return value
    
    # return iterator of keys
    def keys(self):
        for key in self.__listOfkeys:
            yield key

    # return iterator of values
    def values(self):
        for key in self.__listOfkeys:
            yield self.__dictionary[key]

    # return iterator of (key, value) pairs
    def items(self):
        for key in self.__listOfkeys:
            yield (key, self.__dictionary[key])
    
def main():
    sep = "-"*50
    d = OrderedDictionary()
    #Add three key-value pairs
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4

    print("len(d):", len(d))
    print('d[1]: ', d[1]) # Should print 2

    #Update value for key 'b'
    print("Updating d['b'] = 8...")
    d['b'] = 8
    print('d[1]: ', d[1]) # Should print 8
    print(sep)
    print("updating with integer index d[0] = 0. Should update d['a']")
    d[0] = 0 # update using integer index. Should update d['a']
    print("d['a']: ", d['a']) # Should print 0
    print(sep)
    #iterate using __iter__ method
    print("Iterating ...")
    for m in d:
        print(m, end=",")
    print("\n"+sep)

    #iterate using keys() method
    print("Iterating using keys()...")
    for m in d.keys():
        print(m, end=",")
    print("\n"+sep)

    #removing 'b'
    print("Removing 'b'...pop('b')")
    print(d.pop('b')) #should print 8
    print(sep)
    #iterate using values() method
    print("Iterating using values()...")
    for m in d.values():
        print(m, end=",")
    print("\n"+sep)

    #adding 'b' again
    print("adding 'b' again d['b'] = 10")
    d['b'] = 10
    print(sep)
    #removing 'd'
    print("Removing key 'd'...pop(2)")
    print(d.pop(2)) #should print 4
    print(sep)
    #iterate using items() method
    print("Iterating using items()...")
    for m in d.items():
        print(m, end=",")
    print("\n"+sep)

    try:
        print("Trying d[3.0] = 5...")
        d[3.0] = 5 # should raise ValueError
    except Exception as e:
        print(e)
    print(sep)
    try:
        print("Trying d[5]....")
        print(d[5]) # should raise IndexError
    except Exception as e:
        print(e)
    print(sep)
    try:
        print("Trying pop[3.1412]....")
        print(d.pop(3.1412)) # should raise ValueError
    except Exception as e:
        print(e)
    print(sep)
if __name__ == "__main__":
    main()