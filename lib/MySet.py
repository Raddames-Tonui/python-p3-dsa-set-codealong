class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        self.dictionary[value] = True  # Add a value as a key in the dictionary
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()

# Example usage:
my_list = MySet([1, 2, 3, 4, 4, 3, 4, 6, 6, 1])
print(my_list.add(6))  # Output: <__main__.MySet object at 0x...>
print(my_list.delete(9))  # Output: <__main__.MySet object at 0x...>
print(my_list.size())  # Output: 5
