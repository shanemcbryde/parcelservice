from processing import route
from processing.helper import time


# Time complexity: O(n^2)
# Space complexity: O(n)
# Since the number of destinations (m) cannot be greater than the number of packages (n),
# the worst case scenario is that every package is going to a unique destination.
# Therefore, m is equal to n and nm becomes n^2.

# Delivery function.
def deliver(routing_list,
            destination_list,
            truck_list,
            truck_num,
            begin_time,
            mph,
            wrong_address_list,
            package_list,
            load_time,
            wrong_address_time,
            final_run):

    location = 0
    distance_to_hub = 0

    # Update package delivery details and truck miles during delivery.
    truck_item = truck_list.search(truck_num)
    for package_item in routing_list:
        zip_list = destination_list.search(package_item.zip)
        for zip_item in zip_list:
            if package_item.address == zip_item.address:
                distance = zip_item.distances[location]
                truck_item.miles += distance
                package_item.truck_num = truck_item.id
                delivery_time = time.get_time(mph, truck_item.miles, begin_time)
                package_item.delivery_time = delivery_time
                location = int(zip_item.id)
                distance_to_hub = zip_item.distances[0]
                break

    # Any uncorrected wrong address packages are assumed to be loaded onto the final run truck.
    # Determine if there are undelivered wrong address packages on-board and deliver them at the end of the final run.
    if final_run:
        if (route.num_routed + len(wrong_address_list)) == len(package_list):
            for wrong_address in wrong_address_list:
                package_item = package_list.search(wrong_address[0])
                if not package_item.loaded:

                    # Correct the package address data and save the wrong address data to wrong_address_list.
                    # In other words, swap the data.
                    temp_address = package_item.address
                    temp_city = package_item.city
                    temp_state = package_item.state
                    temp_zip = package_item.zip
                    package_item.address = wrong_address[1]
                    package_item.city = wrong_address[2]
                    package_item.state = wrong_address[3]
                    package_item.zip = wrong_address[4]
                    wrong_address[1] = temp_address
                    wrong_address[2] = temp_city
                    wrong_address[3] = temp_state
                    wrong_address[4] = temp_zip
                    zip_list = destination_list.search(package_item.zip)
                    for zip_item in zip_list:
                        if package_item.address == zip_item.address:
                            distance = zip_item.distances[location]
                            truck_item.miles += distance
                            package_item.truck_num = truck_item.id
                            delivery_time = time.get_time(mph, truck_item.miles, begin_time)
                            package_item.delivery_time = delivery_time
                            package_item.available = True
                            package_item.loaded = True
                            package_item.loaded_time = load_time
                            route.num_routed += 1

                            # If the wrong address correction time hasn't passed,
                            # add minutes to delivery_time that the truck must wait before package can be delivered.
                            if wrong_address_time > delivery_time:
                                minute_difference = time.time_difference(wrong_address_time, delivery_time)
                                delivery_time = time.add_minutes(minute_difference, delivery_time)
                                package_item.delivery_time = delivery_time

                            location = int(zip_item.id)
                            distance_to_hub = zip_item.distances[0]
                            break

    truck_item.miles += distance_to_hub
