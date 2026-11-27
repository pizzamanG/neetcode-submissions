class PrefixTree:

    def __init__(self):
        self.dic = {}
        

    def insert(self, word: str) -> None:

        root = self.dic

        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]
        root['#'] = True
       
        


    def search(self, word: str) -> bool:
        root = self.dic
        for char in word:
            if char not in root:
                return False
            root = root[char]
          
        if '#' in root:
            return True
        return False 
        
        



    def startsWith(self, prefix: str) -> bool:
        root = self.dic
        for char in prefix:
            if char not in root:
                return False
            root = root[char]
           
        
        return True
        
        