from random import choice
class RandomizedSet:

    def __init__(self):
        self.sdict = {}
        self.slist = []

    def insert(self, val: int) -> bool:
        if val in self.sdict:
            return False
        # set the new value of dictionary to next index (which is len of slist)
        self.sdict[val] = len(self.slist)
        self.slist.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.sdict:
            return False
        
        # retrieve index of value and update value of last element in list with that index
        index = self.sdict[val]
        self.sdict[val], self.sdict[self.slist[-1]] = self.sdict[self.slist[-1]], self.sdict[val]
        
        # swap index and last element
        self.slist[-1], self.slist[index] = self.slist[index], self.slist[-1]
        
        self.slist.pop()
        del self.sdict[val]
        return True
        
    def getRandom(self) -> int:
        return choice(self.slist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
