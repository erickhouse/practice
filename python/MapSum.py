
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """    
        self.prefix = dict()
        self.hist = set()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.hist:
            strPrefix = ""
            oldVal = self.prefix.get(key)
            for char in key:
                strPrefix += char
                self.prefix[strPrefix] = (self.prefix.get(strPrefix) - oldVal) + val

        else:
            strPrefix = ""
            for char in key:
                strPrefix += char

                if strPrefix in self.prefix.keys():
                    self.prefix[strPrefix] = self.prefix.get(strPrefix) + val
                else:
                    self.prefix[strPrefix] = val

            self.hist.add(key)


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if prefix in self.prefix.keys():
            return self.prefix.get(prefix)
        else:
            return 0


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("ap"))
obj.insert("app", 2)
print(obj.sum("ap"))
