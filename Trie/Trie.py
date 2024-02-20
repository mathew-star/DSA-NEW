class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.end= False
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def char_to_index(self,char):
        return ord(char)-ord('a  ')
    
    def insert(self,word):
        node=self.root
        for ch in word:
            index=self.char_to_index(ch)
            if node.children[index] is None:
                node.children[index]=TrieNode()
            node=node.children[index]
        node.end=True
        
    def search(self,word):
        node=self.root
        for ch in word:
            i=self.char_to_index(ch)
            if node.children[i] is None:
                return False
            node=node.children[i]
        return  node.end 
    
t=Trie()
words = ["apple","app","application"]
for  w in words: t.insert(w)
print(t.search("app"))