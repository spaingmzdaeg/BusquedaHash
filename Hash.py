class hash_table:
    def __init__(self):
        self.table = [None] * 127

    # Hash function
    def Hash_func(self, value):
        key = 0
        for i in range(0, len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value):
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value

    def Search(self, value):
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            return None
        else:
            print("Se encontro el elemento en")
            return hex(id(self.table[hash]))

    def Remove(self, value):
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            print("No se encontro el elemento", value)
        else:
            print("Element with value", value, "deleted")
            self.table[hash] is None;


H = hash_table()
H.Insert("Alo")
H.Insert("Bou")
H.Insert("Col")

print(H.Search("Bou"))
