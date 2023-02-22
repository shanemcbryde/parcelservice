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

![](status1.jpg?raw=true "Single Package Status")

