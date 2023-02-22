from processing.helper import time


# Time complexity: O(n^2)
# Space complexity: O(n)

# Lookup function.
def lookup(package_list,
           truck_list,
           delayed_flight_time,
           wrong_address_time,
           wrong_address_list):

    lookup_id = 0
    total_miles = 0
    lookup_time = None

    # Time complexity: O(n^2)
    # Space complexity: O(n)
    # Since the number of wrong addressed packages (m) is a subset of the number of packages (n),
    # the worst case scenario is that all packages are wrong addressed packages.
    # Therefore, m is equal to n and mn becomes n^2.

    # List details for all packages at the time input by the user including location status and expected delivery time.
    def all_lookup():
        nonlocal package_list
        nonlocal truck_list
        nonlocal delayed_flight_time
        nonlocal wrong_address_time
        nonlocal wrong_address_list
        nonlocal lookup_time

        print('\nSTATUS OF PACKAGES AT: %s' % time.time_to_str(lookup_time))
        print('-'*138)
        print(f"{'ID':<4}{'ADDRESS':<70}{'WEIGHT':<10}{'DEADLINE':<13}{'STATUS':<41}")
        print(f"{'-'*2:<4}{'-'*67:<70}{'-'*7:<10}{'-'*8:<13}{'-'*41:<41}")

        for i in range(1, len(package_list) + 1):
            package = package_list.search(i)
            deadline_time = time.time_to_str(package.deadline)

            if package.delivery_time < lookup_time:
                package_status = 'DELIVERED - AT:'
            else:
                if package.loaded_time < lookup_time:
                    package_status = 'EN ROUTE - DUE:'
                else:
                    package_status = 'HUB - EXPECTED:'

            if deadline_time == '05:00 PM':
                deadline_time = 'EOD'

            address_not_corrected = False
            for wrong_item in wrong_address_list:
                if wrong_item[0] == package.id:
                    if wrong_address_time > lookup_time:
                        address_not_corrected = True
                    break

            print(f'{str(package.id).ljust(4, " ")}', end='')
            if address_not_corrected:
                print(f"{wrong_item[1]:<40}"
                      f"{wrong_item[2]:<18}"
                      f"{wrong_item[3]:<4}"
                      f"{wrong_item[4]:<8}", end='')
            else:
                print(f"{package.address:<40}"
                      f"{package.city:<18}"
                      f"{package.state:<4}"
                      f"{package.zip:<8}", end='')
            print(f"{package.weight:<3}"
                  f"{'KILO':<7}"
                  f"{deadline_time:<13}"
                  f"({str(package.id):<4}{package_status:<17}", end='')

            # Applies to any package that has a wrong address.
            if package.code == 'C' and address_not_corrected:
                print("WRONG ADDRESS)")

            # Applies to any package addressed to a destination that a delayed flight package is addressed to,
            # unless a deadline would be affected.
            elif package.code == 'B' and delayed_flight_time > lookup_time:
                print("DELAYED FLIGHT)")
            else:
                print(f"{time.time_to_str(package.delivery_time):<11}"
                      f"truck {package.truck_num})")

        time_choice()

    # Time complexity: O(n)
    # Space complexity: O(n)
    # Since the number of wrong addressed packages (m) is a subset of the number of packages (n),
    # the worst case scenario is that all packages are wrong addressed packages.
    # Therefore, m is equal to n and m becomes n.

    # List details for package ID at the time input by the user including location status and expected delivery time.
    def id_lookup():
        nonlocal package_list
        nonlocal truck_list
        nonlocal delayed_flight_time
        nonlocal wrong_address_time
        nonlocal wrong_address_list
        nonlocal lookup_time
        nonlocal lookup_id

        print('\nSTATUS OF PACKAGE ID %d AT: %s' % (lookup_id, time.time_to_str(lookup_time)))
        print('-'*138)
        print(f"{'ID':<4}{'ADDRESS':<70}{'WEIGHT':<10}{'DEADLINE':<13}{'STATUS':<41}")
        print(f"{'-'*2:<4}{'-'*67:<70}{'-'*7:<10}{'-'*8:<13}{'-'*41:<41}")

        package = package_list.search(lookup_id)
        deadline_time = time.time_to_str(package.deadline)

        if package.delivery_time < lookup_time:
            package_status = 'DELIVERED - AT:'
        else:
            if package.loaded_time < lookup_time:
                package_status = 'EN ROUTE - DUE:'
            else:
                package_status = 'HUB - EXPECTED:'

        if deadline_time == '05:00 PM':
            deadline_time = 'EOD'

        address_not_corrected = False
        for wrong_item in wrong_address_list:
            if wrong_item[0] == package.id:
                if wrong_address_time > lookup_time:
                    address_not_corrected = True
                break

        print(f'{str(package.id).ljust(4, " ")}', end='')
        if address_not_corrected:
            print(f"{wrong_item[1]:<40}"
                  f"{wrong_item[2]:<18}"
                  f"{wrong_item[3]:<4}"
                  f"{wrong_item[4]:<8}", end='')
        else:
            print(f"{package.address:<40}"
                  f"{package.city:<18}"
                  f"{package.state:<4}"
                  f"{package.zip:<8}", end='')
        print(f"{package.weight:<3}"
              f"{'KILO':<7}"
              f"{deadline_time:<13}"
              f"({str(package.id):<4}{package_status:<17}", end='')

        # Applies to any package that has a wrong address.
        if package.code == 'C' and address_not_corrected:
            print("WRONG ADDRESS)")

        # Applies to any package addressed to a destination that a delayed flight package is addressed to,
        # unless a deadline would be affected.
        elif package.code == 'B' and delayed_flight_time > lookup_time:
            print("DELAYED FLIGHT)")
        else:
            print(f"{time.time_to_str(package.delivery_time):<11}"
                  f"truck {package.truck_num})")

        time_choice()

    # Time complexity: O(1)
    # Space complexity: O(1)
    #
    # Allow user to choose either all packages '0' or an individual package ID.
    def package_choice():
        nonlocal package_list
        nonlocal truck_list
        nonlocal delayed_flight_time
        nonlocal wrong_address_time
        nonlocal wrong_address_list
        nonlocal lookup_id

        print('\nSELECT ALL PACKAGES: 0')
        print('SELECT PACKAGE ID: 1-%d' % len(package_list))
        lookup_id = input('\t(0 OR 1-%d): ' % len(package_list))

        try:
            lookup_id = int(lookup_id)
        except ValueError:
            package_choice()

        if lookup_id == 0:
            all_lookup()
        elif 1 <= lookup_id <= len(package_list):
            id_lookup()
        else:
            package_choice()

    # Time complexity: O(1)
    # Space complexity: O(1)

    # Allow the user to input a time for the lookup function.
    def time_choice():
        nonlocal package_list
        nonlocal truck_list
        nonlocal delayed_flight_time
        nonlocal wrong_address_time
        nonlocal wrong_address_list
        nonlocal lookup_time

        print("\nCHECK STATUS AT GIVEN TIME (or 'q' to quit)")
        lookup_time = input("\tFORMAT (9:25 am): ")

        if lookup_time.lower() in ['q', 'quit']:
            return

        try:
            lookup_time = time.str_to_time(lookup_time)
        except:
            time_choice()

        package_choice()

    # ***************************** BEGIN LOOKUP FUNCTION ****************************

    # List details for all packages including delivery time and on-time status.
    print('\nWestern Governors University Parcel Service\n')
    for i in range(1, len(truck_list) + 1):
        truck_item = truck_list.search(i)
        total_miles += truck_item.miles
        print('Truck %d miles: %.1f' % (i, truck_item.miles))
    print('\tTotal miles: %.1f\n' % total_miles)
    print('DAILY LOCAL DELIVERIES')
    print('-'*131)
    print(f"{'ID':<4}{'ADDRESS':<70}{'WEIGHT':<10}{'DEADLINE':<13}{'STATUS':<31}")
    print(f"{'-'*2:<4}{'-'*67:<70}{'-'*7:<10}{'-'*8:<13}{'-'*34:<34}")

    for i in range(1, len(package_list) + 1):
        package = package_list.search(i)
        deadline_time = time.time_to_str(package.deadline)

        if deadline_time == '05:00 PM':
            deadline_time = 'EOD'

        if package.delivery_time <= package.deadline:
            ontime = 'on-time'
        else:
            ontime = 'LATE'

        print(f'{str(package.id).ljust(4, " ")}'
              f'{package.address.ljust(40, " ")}'
              f'{package.city.ljust(18, " ")}'
              f'{package.state.ljust(4, " ")}'
              f'{package.zip.ljust(8, " ")}'
              f'{package.weight.ljust(3, " ")}'
              f'KILO   '
              f'{deadline_time.ljust(13, " ")}'
              f'({str(package.id).ljust(4, " ")}{ontime}   '
              f'{time.time_to_str(package.delivery_time)}   '
              f'truck {package.truck_num})')

    time_choice()
