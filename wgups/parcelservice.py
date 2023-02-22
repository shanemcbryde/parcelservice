# Shane McBryde, Student ID: 00077514
# Western Governors University
# Data Structures and Algorithms II – C950

from processing import initialize, route, deliver, lookup
from processing.helper import time


# Overall time complexity: O(n^5)
# Overall space complexity: O(n)
# Since the number of trucks (m) cannot be greater than the number of packages (n),
# the worst case scenario is that every package is delivered on a unique truck.
# Therefore, m is equal to n and nm becomes n^2.

# Single, easily accessible location for the necessary data either not found in the provided files
# or data unique to and easily identified for this and any future delivery area and daily package allotment.
destination_csv = 'csv/destination.csv'
package_csv = 'csv/package.csv'
hub_zip = '84107'
start_time = '8:00 AM'
finish_time = '5:00 PM'
delayed_flight_time = '9:05 AM'
wrong_address_time = '10:20 AM'
wrong_address_list = [[9, '410 S State St', 'Salt Lake City', 'UT', '84111']]
delayed_flight = True
wrong_address = True
special_truck = 2
num_zipcodes = 23
num_drivers = 2
num_trucks = 3
capacity = 16
mph = 18

# Convert time strings to datetime.time objects.
delayed_flight_time = time.str_to_time(delayed_flight_time)
wrong_address_time = time.str_to_time(wrong_address_time)
start_time = time.str_to_time(start_time)
finish_time = time.str_to_time(finish_time)

# Create the hash tables for destinations, packages, and trucks.
destination_list = initialize.init_destinations(num_zipcodes, destination_csv)
package_list = initialize.init_packages(finish_time, package_csv)
truck_list = initialize.init_trucks(num_drivers, num_trucks)

# Truck rotation at start time, reverse order.
final_run = False
while route.num_routed < len(package_list):
    for i in range(len(truck_list), 0, -1):
        if (len(package_list) - route.num_routed) <= 16:
            final_run = True
        truck_item = truck_list.search(i)
        truck_num = truck_item.id

        if route.num_routed < len(package_list):

            # When flight delay exists, delay load time for first truck number not associated with
            # packages that must be delivered by a specific truck number.
            if delayed_flight and len(truck_list) > 1 and truck_item.id != special_truck:
                begin_time = time.get_time(mph, 0, delayed_flight_time)
                load_time = time.get_time(mph, truck_item.miles, delayed_flight_time)
                delayed_flight = False
            else:
                begin_time = start_time
                load_time = time.get_time(mph, truck_item.miles, start_time)

            # Create route.
            route_list = route.route(destination_list,
                                     package_list,
                                     truck_num,
                                     load_time,
                                     finish_time,
                                     capacity,
                                     wrong_address_list,
                                     final_run,
                                     special_truck,
                                     wrong_address_time,
                                     delayed_flight_time)

            # Make deliveries.
            deliver.deliver(route_list,
                            destination_list,
                            truck_list,
                            truck_num,
                            begin_time,
                            mph,
                            wrong_address_list,
                            package_list,
                            load_time,
                            wrong_address_time,
                            final_run)

# Provide lookup interface.
lookup.lookup(package_list,
              truck_list,
              delayed_flight_time,
              wrong_address_time,
              wrong_address_list)
