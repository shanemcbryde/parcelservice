A package delivery project, essentially the traveling salesman problem, to determine the best route and delivery distribution for daily local deliveries. Includes a central hub from which deliveries are made, the allocation of multiple delivery vehicles, and the need to contend with several package requirements and real-time restrictions.

## Usage
To get the code run the following from the command line:

```commandline
git clone https://github.com/shanemcbryde/parcelservice.git
```

Change directory to `...\parcelservice\wgups` using:

```commandline
cd parcelservice\wgups
```

From the `wgups` directory where `parcelservice.py` is located run:

```commandline
python parcelservice.py
```

The program will run and display the calculated delivery schedule for the day's packages, as shown here: 

![](deliveries.jpg?raw=true "Daily Local Deliveries")

The status can be checked for any package at a user specified time, as shown here:

![](package2.jpg?raw=true "Single Package Status")

Or, the status of all packages at once at a user specified time, as shown here:

![](status1.jpg?raw=true "All Packages Status")

## Project Description
Scenario: The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day; each package has specific criteria and delivery requirements.

Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in the attached “WGUPS Package File,” will be delivered on time with the least number of miles added to the combined mileage total of all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map” and distances to each location are given in the attached “WGUPS Distance Table.”

While you work on this assessment, take into consideration the specific delivery time expected for each package and the possibility that the delivery requirements—including the expected delivery time—can be changed by management at any time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and what time the delivery occurred.

The intent is to use this solution (program) for this specific location and to use the same program in many cities in each state where WGU has a presence. As such, you will need to include detailed comments, following the industry-standard Python style guide, to make your code easy to read and to justify the decisions you made while writing your program.

Assumptions:

1.	Each truck can carry a maximum of 16 packages.
2.	Trucks travel at an average speed of 18 miles per hour.
3.	Trucks have a “infinite amount of gas” with no need to stop.
4.	Each driver stays with the same truck as long as that truck is in service.
5.	Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when all 40 packages have been delivered.
6.	Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the trucks).
7.	There is up to one special note for each package.
    - Certain packages must be delivered by a specified truck.
    - Several packages must be delivered by a specified time.
    - Several packages must be delivered together during the same run and on the same truck.
    - Several packages will have a flight delay and not arrive at the hub until a specified time.
9.	The wrong delivery address for package #9 won't be corrected until 10:20 a.m.
10.	The package ID is unique; there are no collisions.
11.	No further assumptions exist or are allowed.


