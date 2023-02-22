truck_driver = 0


# Time complexity: O(1)
# Space complexity: O(1)

# Truck hash table and functions.
class Truck:
    def __init__(self, 
                 id,
                 driver):
        self.id = id
        self.driver = driver
        self.miles = 0.0
        

# Time complexity: O(1)
# Space complexity: O(1)

# trucks are hashed by the truck number created in the file parcelservice.
# The size of the truck table is determined by the pairing of trucks and drivers.
class TruckTable:
    def __init__(self, size):
        self.table = []
        for i in range(size):
            self.table.append([])

    def __len__(self):
        return truck_driver

    def _get_hash(self, key):
        return (key - 1) % len(self.table)

    def add(self, key, value):
        hash_key = self._get_hash(key)
        self.table[hash_key] = value

    def delete(self, key):
        global truck_driver
        hash_key = self._get_hash(key)
        for i, it in enumerate(self.table[hash_key]):
            if it.key == key:
                del self.table[hash_key][i]
                truck_driver -= 1

    def search(self, key):
        hash_key = self._get_hash(key)
        return self.table[hash_key]
