
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        list = self.table[key_hash]
        if list is None:
            return None
        
        pair_to_remove = None
        for pair in list:
            if pair[0] == key:
                pair_to_remove = pair

        if pair_to_remove:
            list.remove(pair_to_remove)
        return pair_to_remove[1]
        

def main():
    hash_table = HashTable(5)
    hash_table.insert("a", 3)
    print(hash_table.get("a"))
    hash_table.insert("a", 35)
    print(hash_table.delete("a"))
    print(hash_table.get("a"))


if __name__ == "__main__":
    main()