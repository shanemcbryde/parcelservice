num_packages = 0


# Time complexity: O(1)
# Space complexity: O(1)

# Package hash table and functions.
class Package:
    def __init__(self,
                 id,
                 address,
                 city,
                 state,
                 zipcode,
                 deadline,
                 weight,
                 code,
                 message,
                 available):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipcode
        self.deadline = deadline
        self.weight = weight
        self.code = code
        self.message = message
        self.available = available
        self.loaded = False
        self.truck_num = 0
        self.loaded_time = None
        self.delivery_time = None


# Time complexity: O(1)
# Space complexity: O(1)

# Packages are hashed by package ID so the size of the package table is equal to the number of packages.
class PackageTable:
    def __init__(self, size):
        self.table = []
        for i in range(size):
            self.table.append([])

    def __len__(self):
        return num_packages

    def _get_hash(self, key):
        return (key - 1) % len(self.table)

    def add(self, key, value):
        hash_key = self._get_hash(key)
        self.table[hash_key] = value

    def delete(self, key):
        global num_packages
        hash_key = self._get_hash(key)
        for i,it in enumerate(self.table[hash_key]):
            if it.key == key:
                del self.table[hash_key][i]
                num_packages -= 1

    def search(self, key):
        hash_key = self._get_hash(key)
        return self.table[hash_key]
