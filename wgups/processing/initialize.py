import csv
from tables import destination, package, truck
from processing.helper import time


# Time complexity: O(n^2)
# Space complexity: O(n)
# Since the number of destinations (m) cannot be greater than the number of packages (n),
# the worst case scenario is that every package is going to a unique destination.
# Therefore, m is equal to n and m^2 becomes n^2.

# Initialize the destination objects and add them to the destination hash table.
def init_destinations(num_zipcodes, destination_csv):
    with open(destination_csv) as destination_list:
        rows = list(csv.reader(destination_list, delimiter=','))
        destination.num_destinations = len(rows) - 1

        # Complete the missing distances within the distances portion of the provided destination data.
        for i in range(1, destination.num_destinations):
            j = i + 3
            for m in range(i + 1, destination.num_destinations + 1):
                n = m + 3
                rows[i][n] = rows[m][j]

        destinations = destination.DestinationTable(num_zipcodes)
        row_num = 0
        for row in rows:
            row_num += 1
            if row_num > 1:
                id = row[0]
                name = row[1]
                address = row[2]
                zipcode = row[3]
                distances = []
                for i in range(4, destination.num_destinations + 4):
                    distances.append(float(row[i]))

                destination_item = destination.Destination(
                    id,
                    name,
                    address,
                    zipcode,
                    distances
                )
                destinations.add(zipcode, destination_item)

    return destinations

# Time complexity: O(n)
# Space complexity: O(n)

# Initialize the package objects and add them to the package hash table.
def init_packages(finsh_time, package_csv):
    with open(package_csv) as package_list:
        rows = list(csv.reader(package_list, delimiter=','))
        package.num_packages = len(rows)
        packages = package.PackageTable(package.num_packages)
        for row in rows:
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            if row[5] == 'EOD':
                deadline = finsh_time
            else:
                deadline = time.str_to_time(row[5])
            weight = row[6]
            code = row[7]
            message = row[8]
            if row[7] == 'B' or row[7] == 'C':
                available = False
            elif row[7] == 'A':
                available = False
            else:
                available = True

            package_item = package.Package(
                id,
                address,
                city,
                state,
                zipcode,
                deadline,
                weight,
                code,
                message,
                available,
            )
            packages.add(id, package_item)

    return packages

# Time complexity: O(n)
# Space complexity: O(n)
# Since the number of trucks (m) cannot be greater than the number of packages (n),
# the worst case scenario is that every package is delivered on a unique truck.
# Therefore, m is equal to n and m becomes n.

# Initialize the truck objects and add them to the truck hash table.
# The number of available trucks is determined by the lesser value of either trucks or drivers.
def init_trucks(num_drivers, num_trucks):
    truck.truck_driver = min(num_drivers, num_trucks)
    trucks = truck.TruckTable(truck.truck_driver)
    for i in range(1, len(trucks) + 1):
        truck_item = truck.Truck(i, i)
        trucks.add(i, truck_item)

    return trucks
