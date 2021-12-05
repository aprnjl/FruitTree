# Assignment 10.1: Your Own Class
## Name: Pranjal Agrawal
## Source File: fruit_tree.py
[Link to the Project Repository on GitHub: https://github.com/aprnjl/FruitTree](https://github.com/aprnjl/FruitTree)

## Class Documentation

### Description of the Class
The ‘fruit_tree.py’ script implements a FruitTree class that represents a fruit tree which is capable of producing a certain maximum number of fruits per day when the suggested watering frequency per week is followed. If the watering frequency is more or less than the suggested frequency, then the number of fruits produced by the tree every day falls down. The number of fruits produced by a tree is proportional to its health where health can vary from 0.0 to 1.0 (where 1.0 means perfect health). The health of a tree is 1.0 when the watering done during the last one week is the same as suggested. The health goes down in a linear fashion becoming 0.0 if the watering frequency is 0 or if the watering frequency is double of the suggested watering frequency.

### Description of the Class and Data Variables
* **total_fruits**: Class variable that keeps count of all the fruits produced by all the trees since the beginning or since the time this variable was reset.

* **__identifier**: Data variable of type string that is used to identify the tree.

* **__watering_frequency**: Data variable of type int that stores the suggested watering frequency per week for the tree. Should be a number between 1 and 7.

* **__max_fruits_per_day**: Data variable of type int that stores the maximum number of fruits per day that the tree can produce.

* **__health**: Data variable of type float that represents the tree's health. Can be a fraction between 0.0 and 1.0, where 1.0 represents perfect health.

* **__watered_days**: Data variable of type list that shows how many times the tree was watered every day during the past one week. The first index (index 0) represents today, index 1 represents yesterday and so on...

* **__num_fruits**: Data variable of type int that keeps count of the total number of fruits produced by the tree since it was created (or since it was last reset [see the reset method]).

### Description of the Methods
* **__init__(self, identifier, watering_frequency=1, max_fruits_per_day=1)**: Sets up the object with the specified identifier, watering frequency (default is 1 per week) and max fruits produced per day (default is 1 per day). Also resets the other data variables to the starting condition. Input arguments are: tree identifier (str), watering frequency (an int between 1 and 7), and maximum number of fruits the tree can produce per day (int).

* **reset(self)**: Reset the condition of the tree to the starting condition by resetting the three data variables __health to 1.0, __watered_days to a list of 0’s, and __num_fruits to 0.


* **get_identifier(self)**: Takes no input argument. Returns the identifier that identifies the tree.

* **get_watering_frequency(self)**: Takes no input argument. Returns the suggested watering frequency per week for the tree.

* **get_max_fruits_per_day(self)**: Takes no input argument. Returns the maximum number of fruits that can be produced per day by the tree.

* **get_health(self)**: Takes no input argument. Returns the health of the tree (a number ranging from 0.0 to 1.0). A value of 1.0 represents perfect health.

* **get_watered_days(self)**: Takes no input argument. Returns the watering history over the past one week (7 days) as a list. The index 0 represents today, index 1 represents yesterday and so on...

* **get_num_fruits(self)**: Takes no input argument. Returns the total number of fruits produced by the tree since it was created (or since it was last reset [see the reset method]).

* **set_max_fruits_per_day(self, max_fruits_per_day)**: Set the maximum number of fruits that can be produced by this tree when watered according to suggested watering frequency. Input argument is maximum number of fruits per day the tree can produce (int)

* **set_watering_frequency(self, watering_frequency)**: Sets the suggested watering frequency of this tree to enable it to produce maximum fruits it is capable of producing. Input argument is the suggested watering frequency per week (an int between 1 and 7).

* **water(self)**: Water the tree. Increments the number of times the tree is watered today (item 0 of watered_days list) by 1. Takes no input argument. Returns no value.

* **begin_day(self)**: Starts the new day by shifting the list of watered days. Takes no input argument.  Returns no value.

* **end_day(self)**: Updates the tree's health and the number of fruits it has produced by the end of the day. Takes no input argument. Returns no value.

* **update_health(self)**: Updates the health of the tree by looking at the list of watered days and how close it is to suggested watering frequency. The health is 1.0 if the watering frequency is the same as suggested watering frequency, else  it is scaled down linearly, with health becoming 0.0 if it is watered 0  times per week or watered twice the suggested watering frequency. Takes no input argument. Returns no value.

* **update_fruits(self)**: Produces fruits proportional to its current health and maximum number of fruits it can produce. _Rounds any fractional fruits to the closest whole number._ Adds the fruits produced to the total number of fruits produced by the tree so far. Also adds the fruits produced to the class variable total_fruits that represents all the fruits produced by all the trees so far. Takes no input argument. Returns no value.

* **update_watered_days(self)**: Removes the oldest day from the list of watered days and adds a new day to the front of the list. Represents moving on to the next day. Takes no input argument. Returns no value.

* **__str__(self)**: Returns a string version representing the tree. Takes no input argument.

## Demo Program

### Description of the Demo Program
The demo program is the main function in the ‘fruit_tree.py’ file. The program creates two FruitTree objects-an apple tree and an orange tree-by passing each of them an identifier and using the default values of watering frequency and maximum fruits per day. The program then uses the set methods set_max_fruits_per_day() and set_watering_frequency() for each tree. The apple tree object’s max fruits produced per day is set to 2 and watering frequency is set to 3 times a week. The orange tree object’s max fruits produced per day is set to 3 and watering frequency is set to 2 times a week. 

The program then tries out 3 different watering schedules for each tree for one week at a time. In the first watering schedule, both trees are watered the correct amount according to their suggested watering frequency for 1 week. In the second watering schedule that represents under-watering, both trees are watered 1 time less than their suggested watering frequency per week. In the third schedule that represents over-watering, the trees are watered 1 time more than their suggested watering frequency per week. For each watering schedule, the program prints out the daily condition of each tree, including the days it has been watered so far during the last one week, its current health, and the number of fruits the tree has produced so far. At the end of the week, the program also prints out the total number of fruits produced from all the trees combined. From the program’s output, we can see that watering according to the suggested watering frequency gives the most fruits, while over-watering as well as under-watering give fewer total number of fruits.

### Instructions on Running the Demo Program

To run the demo program, follow these steps:
* Download the file ‘fruit_tree.py’
* Go to the directory where the downloaded file exists.
* Run either of the following commands: 
    * py fruit_tree.py 
    * python3 fruit_tree.py


