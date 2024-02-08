class Hash:
    def __init__(self,size=10):
        self.size=size
        self.bucket=[None]*size
    def hash_fuc(self,key):
        return hash(key) % self.size
    
    def put(self,key,value):
        index=self.hash_fuc(key)
        if self.bucket[index] is None:
            self.bucket[index]=[]
        self.bucket[index].append((key,value))

    def get(self, key):
        index = self.hash_fuc(key)
        bucket = self.bucket[index]
        if bucket:
            for k, v in bucket:
                if k == key:
                    return v
        return None

hash_table = Hash()
hash_table.put("name", "John")
hash_table.put("age", 25)
print(hash_table.get("name"))  