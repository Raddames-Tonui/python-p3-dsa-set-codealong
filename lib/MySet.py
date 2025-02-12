def first_repeated_value(list):
  # create a Set to keep track of values we've seen
  number_set = set()
  # iterate over each element from the list
  for i in range (0, len(list)):

    # if we've already seen a value, we've found the duplicate!
    if list[i] in number_set:
        return list[i]
    # otherwise, add the value to our set
    number_set.add(list[i])
  # return None if we reach the end and haven't found our value
  return None

print(first_repeated_value([1,2,3,3,4,4]))
# => 3

# USING DICTIONARY
    
class MyDict:        
    def __init__(self, enumerable=[]):  
        self.dictionary = {}  
        for value in enumerable:  
            self.dictionary[value] = True  # Store unique values as keys  
    
    def __repr__(self):  
        return f"MyDict({list(self.dictionary.keys())})"  # Corrected the name from MySet to MyDict  
    
    def has(self, value):  
        return value in self.dictionary  # Check for the presence of value  
      
    def add(self, value):  
        self.dictionary[value] = True  # Add unique value  
        return self  # Method chaining enabled  
    
    def delete(self, value):  
        self.dictionary.pop(value, None)  # Safely remove value  
        return self  
    
    def size(self):  
        return len(self.dictionary)  # Number of unique values  
    
    def clear(self):  
        self.dictionary.clear()  # Clear all elements  
        return self

# USING SETS

class MySet:
    def __init__(self, enumerable =[]):
      self.set = set()
      for value in enumerable:
         self.set.add(value)

    def has(self, value):
        return value in self.set

    def add(self, value):
       self.set.add(value)
       return self

    def delete(self, value):
       self.set.discard(value)              
       return self
    
    def size(self):
       return len(self.set)
    
    def clear(self):
       self.set.clear()
       return  self
    
    def __repr__(self):
       return f"MySet({list(self.set)})"
       

dset = MyDict([1,2,3,5,6,4,2,3])
print(dset.dictionary)
print(dset.add(7))
print(dset)
print(dset.clear())
print(f"\n")

myset =MySet([1,2,3,5,6,4,2,3])
print(myset.set)
print(myset.add(7))
print(myset)
print(myset.clear())
