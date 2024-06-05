class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        if value not in self.dictionary:
            self.dictionary[value] = True
            return (f"{value} added")
        else:
            return (f"{value} already in set")
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)

my_list = MySet([1,2,3,4,4,3,4,6,6,1])
print(my_list.add(6))