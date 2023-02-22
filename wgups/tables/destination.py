num_destinations = 0


# Time complexity: O(1)
# Space complexity: O(1)

# Destination hash table and functions.
class Destination:
    def __init__(self,
                 id,
                 name,
                 address,
                 zipcode,
                 distances):
        self.id = id
        self.name = name
        self.address = address
        self.zip = zipcode
        self.distances = distances


# Time complexity: O(1)
# Space complexity: O(1)

# Destinations are hashed by zip code so the size of the destination table is equal to the number of zip codes.
# Chaining is used to handle collisions and a list is used for each bucket to store all destinations within a zip code.
class DestinationTable:
    def __init__(self, size):
        self.table = []
        for i in range(size):
            self.table.append([])

    def __len__(self):
        return num_destinations

    def _get_hash(self, key):
        return (int(key[3:4])) % len(self.table)

    def add(self, key, value):
        hash_key = self._get_hash(key)
        zip_list = self.table[hash_key]
        zip_list.append(value)

    def delete(self, key, value):
        global num_destinations
        hash_key = self._get_hash(key)
        zip_list = self.table[hash_key]
        zip_list.remove(value)
        num_destinations -= 1

    def search(self, key):
        hash_key = self._get_hash(key)
        zip_list = self.table[hash_key]
        return zip_list


