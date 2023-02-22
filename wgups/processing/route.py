num_routed = 0


# Time complexity: O(n^3)
# Space complexity:O(n)

# Routing functions.
# Populate bundled and delayed lists. Prioritize deadline packages first.
def route(destination_list,
          package_list,
          truck_num,
          load_time,
          end_time,
          capacity,
          wrong_address_list,
          final_run,
          special_delivery_num,
          wrong_address_time,
          delayed_flight_time):
    global num_routed
    closest_destination = None
    closest_package = None
    bundle_package = False
    bundle_return_trip = False
    present_location = 0
    bundled_count = 0
    loaded_count = 0
    index_sorted = 0
    bundled = []
    delayed = []
    loaded = []

    # Time complexity: O(n^2)
    # Space complexity: O(n)
    # Since the number of wrong addressed packages (m) is a subset of the number of packages (n)
    # and the number of delayed packages (k) is a subset of the number of packages (n).
    # the worst case scenario is that every package is in the subsets.
    # Therefore, m is equal to n and k is equal to n and (nm + nk) becomes n^2.

    # Attend to special notes requirements
    def special_notes():
        nonlocal package_list
        nonlocal bundled
        nonlocal delayed

        # Allow truck 2 packages to only be available while loading truck 2.
        for i in range(1, len(package_list) + 1):
            package_item = package_list.search(i)
            if package_item.code == 'A' and not package_item.loaded:
                if truck_num == special_delivery_num:
                    package_item.available = True
                else:
                    package_item.available = False

            # If delayed packages haven't arrived at the HUB yet, add them to the delayed list.
            if not package_item.available:
                if package_item.code == 'B':
                    if delayed_flight_time <= load_time:
                        package_item.available = True
                    else:
                        delayed.append(package_item)

                # If it is past the time to correct wrong addresses, correct the address
                # and save the incorrect address back to wrong_address_list.
                elif package_item.code == 'C':
                    if wrong_address_time <= load_time:
                        package_item.available = True
                        for wrong_address in wrong_address_list:
                            if wrong_address[0] == package_item.id:
                                package_item.address, wrong_address[1] = wrong_address[1], package_item.address
                                package_item.city, wrong_address[2] = wrong_address[2], package_item.city
                                package_item.state, wrong_address[3] = wrong_address[3], package_item.state
                                package_item.zip, wrong_address[4] = wrong_address[4], package_item.zip
            else:
                # Add packages that must be delivered together to bundled list.
                if package_item.code == 'D' and not package_item.loaded:
                    bundled.append(package_item)

        # Identify delayed packages not available at load time and, if it doesn't disrupt a deadline,
        # add all other packages going to the same address to delayed list.
        for delayed_item in delayed:
            for i in range(1, len(package_list) + 1):
                package_item = package_list.search(i)
                if package_item.address == delayed_item.address:
                    if package_item.deadline > delayed_flight_time:
                        package_item.code = 'B'
                        package_item.available = False

    # Time complexity: O(n)
    # Space complexity: O(n)

    # Identify which available packages have the earliest delivery priority and return the list.
    def priority():
        nonlocal package_list
        nonlocal end_time
        earliest_time = end_time
        priority_items = []

        for i in range(1, len(package_list) + 1):
            package_item = package_list.search(i)
            if package_item.available and not package_item.loaded:
                if package_item.deadline <= earliest_time:
                    if package_item.deadline < earliest_time:
                        priority_items = []
                    earliest_time = package_item.deadline
                    priority_items.append(package_item)
        return priority_items

    # Time complexity: O(n^2)
    # Space complexity: O(n)
    # Since the number of destinations (m) cannot be greater than the number of packages (n),
    # the worst case scenario is that every package is going to a unique destination and m is equal to n.
    # Therefore, m is equal to n and nm becomes n^2.

    # Alternative to closest() functions, used after bundled packages run and truck capacity has not been reached.
    def return_trip():
        nonlocal package_list
        nonlocal destination_list
        nonlocal present_location
        nonlocal closest_destination
        nonlocal closest_package
        nonlocal bundle_package
        distance = 100

        for i in range(1, len(package_list) + 1):
            package_item = package_list.search(i)
            if package_item.available and not package_item.loaded:
                zip_list = destination_list.search(package_item.zip)
                for destination_item in zip_list:
                    if destination_item.address == package_item.address:
                        destination_distance = destination_item.distances[present_location]
                        hub_distance = destination_item.distances[0]
                        total_distance = destination_distance + hub_distance
                        if total_distance < distance:
                            distance = total_distance
                            closest_destination = destination_item
                            closest_package = package_item
                        break

    # Time complexity: O(n^2)
    # Space complexity: O(n)
    # Since the number of destinations (m) cannot be greater than the number of packages (n),
    # the worst case scenario is that every package is going to a unique destination.
    # Therefore, m is equal to n and nm becomes n^2.

    # Greedy algorithm is used to determine which package from the priority packages list
    # is the closest to the present location.
    def closest():
        nonlocal priority_packages
        nonlocal destination_list
        nonlocal present_location
        nonlocal closest_destination
        nonlocal closest_package
        nonlocal bundle_package
        distance = 100

        for package_item in priority_packages:
            if package_item.available and not package_item.loaded:
                zip_list = destination_list.search(package_item.zip)
                for destination_item in zip_list:
                    if destination_item.address == package_item.address:
                        if destination_item.distances[present_location] < distance:
                            distance = destination_item.distances[present_location]
                            closest_destination = destination_item
                            closest_package = package_item
                            if closest_package.code == 'D':
                                bundle_package = True
                        break

    # Time complexity: O(n)
    # Space complexity: O(n)

    # Identify and return the available packages within the same zip code as the present package.
    def samezip():
        nonlocal package_list
        nonlocal closest_destination
        nonlocal bundle_package
        samezip_packages = []

        for i in range(1, len(package_list) + 1):
            package_item = package_list.search(i)
            if package_item.available and not package_item.loaded and package_item.zip == closest_destination.zip:
                samezip_packages.append(package_item)
                if package_item.code == 'D':
                    bundle_package = True

        return samezip_packages

    # Time complexity: O(n)
    # Space complexity: O(n)
    # Since the number of packages that are loaded (m) cannot be greater than the number of packages,
    # the worst case scenario is that all packages are loaded.
    # Therefore, m is equal to n and m becomes n.

    # Load closest package onto truck for delivery.
    def loading():
        nonlocal closest_package
        nonlocal truck_num
        global num_routed
        nonlocal bundled_count
        nonlocal loaded
        nonlocal loaded_count
        nonlocal bundle_return_trip

        loaded.append(closest_package)
        closest_package.truck_num = truck_num
        closest_package.loaded_time = load_time
        closest_package.loaded = True
        num_routed += 1
        loaded_count += 1
        if closest_package.code == 'D':
            bundled_count += 1
        if 0 < bundled_count == len(bundled):
            bundle_return_trip = True

    # Time complexity: O(n^3)
    # Space complexity: O(n)
    # Since the number of packages that are loaded (m) is a subset of the number of packages (n)
    # and the number destinations (k) cannot be greater than the number of packages (n),
    # the worst case scenario is that all packages are loaded and each package is going to a unique destination.
    # Therefore, m is equal to n and k is equal to n and mmk becomes n^3.

    # Sort packages using greedy algorithm within a zip code
    # beginning at either the HUB or the last location of the previous zip code.
    def sort_load():
        nonlocal closest_package
        nonlocal destination_list
        nonlocal present_location
        nonlocal index_sorted
        nonlocal loaded
        shortest_distance = 0
        temp_distance = 0
        location = present_location

        zip_list = destination_list.search(closest_package.zip)
        for i in range(index_sorted, len(loaded) - 1):
            index_shortest = i
            for idestination_item in zip_list:
                if idestination_item.address == loaded[i].address:
                    shortest_distance = idestination_item.distances[location]
                    temp_destination = int(idestination_item.id)
                    break

            for j in range(i + 1, len(loaded)):
                for jdestination_item in zip_list:
                    if jdestination_item.address == loaded[j].address:
                        temp_distance = jdestination_item.distances[location]
                        break

                if temp_distance < shortest_distance:
                    index_shortest = j
                    shortest_distance = temp_distance
                    temp_destination = int(jdestination_item.id)

            temp = loaded[i]
            loaded[i] = loaded[index_shortest]
            loaded[index_shortest] = temp
            location = temp_destination

        for destination_item in zip_list:
            if destination_item.address == loaded[len(loaded) - 1].address:
                present_location = int(destination_item.id)
                break

        index_sorted = len(loaded)

    # ***************************** BEGIN PACKAGE SELECTION AND SORTING OF ROUTE ****************************

    # Processing of special notes packages.
    special_notes()

    # Key items...
    # bundled: List of packages that must be delivered on the same truck during the same run.
    # bundle_return_trip: After bundled packages are selected and if truck capacity has not been reached.
    # priority_packages: List of packages from which to choose the closest package,
    # prioritized by earliest deadline packages then next earliest deadline packages then remaining EOD packages,
    # will contain bundled list if bundled list includes deadline packages.

    # Identify run: bundled packages, bundled return trip, or priority package run. Retrieve appropriate packages.
    while loaded_count < capacity and num_routed < len(package_list):
        if bundle_return_trip:
            return_trip()
        else:
            if bundle_package and bundled_count < len(bundled):
                priority_packages = bundled
                bundle_package = False
            else:
                priority_packages = priority()
                if len(priority_packages) == 0:
                    break

            # Determines the closest package from the present location out of priority packages.
            closest()

        # Load the closest package onto the truck.
        loading()

        # Finds available packages going to the same zip code and, starting with packages that have the same
        # address, load each onto the truck until capacity is reached.
        if loaded_count < capacity and num_routed < len(package_list):
            samezip_packages = samezip()
            for package_item in samezip_packages:
                closest_package = package_item
                if loaded_count < capacity and num_routed < len(package_list):
                    if package_item.address == closest_destination.address:
                        loading()
                        samezip_packages.remove(package_item)
            for package_item in samezip_packages:
                closest_package = package_item
                if loaded_count < capacity and num_routed < len(package_list):
                    loading()

        # Sorts the loaded packages within the zip code.
        sort_load()

        # Unless it is the final run, do not allow long runs between any three consecutive package deliveries
        # along the route. If an offending package is found, offload the package and continue package selection.
    if not final_run:
        distances_list = []
        from_destination = None
        to_destination = None
        for i in range(1, len(loaded)):
            from_package = loaded[i - 1]
            to_package = loaded[i]
            destination_zip = destination_list.search(from_package.zip)
            for destination in destination_zip:
                if from_package.address == destination.address:
                    from_destination = destination
                    break
            destination_zip = destination_list.search(to_package.zip)
            for destination in destination_zip:
                if to_package.address == destination.address:
                    to_destination = destination
                    break
            distance = from_destination.distances[int(to_destination.id)]
            distances_list.append(distance)

        for i in range(1, len(distances_list)):
            if distances_list[i] + distances_list[i-1] > 9:
                loaded[i].available = True
                loaded[i].loaded = False
                loaded[i].truck_num = 0
                loaded_count -= 1
                num_routed -= 1
                loaded.remove(loaded[i])

    return loaded
