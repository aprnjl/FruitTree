'''
Name: Pranjal Agrawal

Assignment 10.1: Your Own Class
fruit_tree.py

Description: This script implements a FruitTree class that represents a fruit tree 
which is capable of producing certain maximum number of fruits per day when the 
suggested watering frequency per week is followed. If the watering frequency is 
more or less than the suggested frequency, then the number of fruits produced by 
the tree every day falls down. The number of fruits produced by a tree is proportional 
to its health where health can vary from 0.0 to 1.0 (where 1.0 means perfect health). 
The health of a tree is 1.0 when the watering done during the last one week is the same 
as suggested. The health goes down in a linear fashion becoming 0.0 if the watering 
frequency is 0 or if the watering frequency is double of the suggested watering 
frequency.
'''

import random

class FruitTree:
    '''
    A class that represents a fruit tree that grows fruits every day and requires
    a certain watering frequency.
    '''
    
    total_fruits = 0
    '''
    total_fruits is a class variable that keeps count of all the fruits produced by 
    all the trees since the beginning or since the time this variable was reset.
    '''

    def __init__(self, identifier, watering_frequency=1, max_fruits_per_day=1):
        '''
        Sets up the object with the specified identifier, watering frequency (default
        is 1 per week) and max fruits produced per day (default is 1 per day). Also 
        resets the other data variables to the starting condition.
        Input arguments are: tree identifier (str), watering frequency (an int between 
        1 and 7), and maximum number of fruits the tree can produce per day (int).
        '''
        
        self.__identifier = identifier 
        '''
        Data variable of type string that is used to identify the tree.
        '''

        if watering_frequency < 1 or watering_frequency > 7: # incorrect watering frequency
            print(f"Invalid watering frequency {watering_frequency} specified for {self.__identifier}. Setting it to 1.")
            self.__watering_frequency = 1
        else: self.__watering_frequency = watering_frequency # # of days per week
        '''
        Data variable of type int that stores the suggested watering frequency 
        per week for the  tree. Should be a number between 1 and 7.
        '''

        self.__max_fruits_per_day = max_fruits_per_day
        '''
        Data variable of type int that stores the maximum number of fruits 
        per day that the tree can produce.
        '''

        self.reset() 
        '''
        Method called to reset the condition of the tree to the starting condition 
        by resetting the three data variables __health, __watered_days, and __num_fruits.
        '''

    def reset(self):
        '''
        Reset the condition of the tree to the starting condition by resetting the 
        three data variables __health to 1.0, __watered_days to a list of 0’s, and 
        __num_fruits to 0.
        '''
        self.__health = 1.0 
        '''
        Data variable of type float that represents the tree's health. Can be a fraction 
        between 0.0 and 1.0, where 1.0 representing perfect health.
        '''

        self.__watered_days = [0, 0, 0, 0, 0, 0, 0] 
        '''
        Data variable of type list that shows how many times the tree was watered every day 
        during the past one week. The first index (index 0) represents today, index 1 represents
        yesterday and so on...
        '''
        self.__num_fruits = 0 
        '''
        Data variable of type int that keeps count of the total number of fruits prodcued 
        by the tree since it was created (or since it was last reset).
        '''

    def get_identifier(self):
        '''
        Takes no input argument.
        Returns the identifier that identifies the tree. 
        '''
        return self.__identifier

    def get_watering_frequency(self):
        '''
        Takes no input argument.
        Returns the suggested watering frequency per week for the tree.
        '''
        return self.__watering_frequency

    def get_max_fruits_per_day(self):
        '''
        Takes no input argument.
        Returns the maximum number of fruits that can be produced per day by the tree.
        '''
        return self.__max_fruits_per_day

    def get_health(self):
        '''
        Takes no input argument.
        Returns the health of the tree (a number ranging from 0.0 to 1.0). 
        A value of 1.0 represents perfect health.
        '''
        return self.__health
    
    def get_watered_days(self):
        '''
        Takes no input argument.
        Returns the watering history over the past one week (7 days) as a list. 
        The index 0 represents today, index 1 represents yesterday and so on...
        '''
        return self.__watered_days

    def get_num_fruits(self):
        '''
        Takes no input argument.
        Returns the total number of fruits produced by the tree since it 
        was created (or since it was last reset).
        '''
        return self.__num_fruits

    def set_max_fruits_per_day(self, max_fruits_per_day):
        '''
        Set the maximum number of fruits that can be produced by this tree 
        when watered according to suggested watering frequency.
        Input argument is maximum number of fruits per day the tree can produce (int)
        '''
        self.__max_fruits_per_day = max_fruits_per_day

    def set_watering_frequency(self, watering_frequency):
        '''
        Sets the suggested watering frequency of this tree to enable it to 
        produce maximum fruits it is capable of producing.
        Input argument is the suggested watering frequency per week (an int
        between 1 and 7).
        '''
        if watering_frequency < 1 or watering_frequency > 7: # incorrect watering frequency
            print(f"Invalid watering frequency {watering_frequency} specified for {self.__identifier}. Setting it to 1.")
            self.__watering_frequency = 1
        else: self.__watering_frequency = watering_frequency

    def water(self):
        '''
        Water the tree. Increments the number of times the tree is watered today 
        (item 0 of watered_days list) by 1.
        Takes no input argument.
        Returns no value.
        '''
        self.__watered_days[0] += 1

    def begin_day(self):
        '''
        Starts the new day by shifting the list of watered days.
        Takes no input argument.
        Returns no value.
        '''
        self.update_watered_days()

    def end_day(self):
        '''
        Updates the tree's health and the number of fruits it has produced
        by the end of the day.
        Takes no input argument.
        Returns no value.
        '''
        self.update_health()
        self.update_fruits()

    def update_health(self):
        '''
        Updates the health of the tree by looking at the list of watered
        days and how close it is to suggested watering frequency. The health is
        1.0 if the watering frequency is the same as suggested watering frequency, 
        else it is scaled down linearly, with health becoming 0.0 if it is watered 0
        times per week or watered twice the suggested watering frequency.
        Takes no input argument.
        Returns no value.
        '''
        x = sum(self.__watered_days)
        if x <= self.__watering_frequency: # scale health up linearly from 0 to 1
            self.__health = x / self.__watering_frequency
        elif x <= 2 * self.__watering_frequency: # scale health down linearly from 1 to 0
            self.__health = 2 - (x / self.__watering_frequency)
        else: # set health to 0 if watered more than twice the suggested watering frequency
            self.__health = 0

    def update_fruits(self):
        '''
        Produces fruits proportional to its current health and maximum 
        number of fruits it can produce. Rounds any fractional fruits to the 
        closest whole number. Adds the fruits produced to the total number 
        of fruits produced by the tree so far. Also adds the fruits produced 
        to the class variable total_fruits that represents all the fruits 
        produced by all the trees so far.
        Takes no input argument.
        Returns no value.
        '''
        # calculate fruits and round the fraction as we can only have whole fruits
        new_fruits = round(self.__max_fruits_per_day * self.__health) 
        self.__num_fruits += new_fruits # add the fruits produced to the total fruits produced by the tree
        FruitTree.total_fruits += new_fruits # add the fruits produced to the total fruits produced by all the trees

    def update_watered_days(self):
        '''
        Removes the oldest day from the list of watered days and adds a new day to 
        the front of the list. Represents moving on to the next day.
        Takes no input argument.
        Returns no value.
        '''
        if len(self.__watered_days) >= 1:
            self.__watered_days.pop(-1) # remove 7th day
            self.__watered_days.insert(0, 0) # add a new day

    def __str__(self):
        '''
        Returns a string version representing the tree.
        Takes no input argument.
        '''
        return f"\t{self.__identifier}:\tWatered Days = {self.__watered_days}\tHealth = {self.__health:.1f}\tTotal Fruits = {self.__num_fruits}"


def main():
    '''
    The main function that is the Demo Program. It creates two trees and tries out 3 different
    watering schedules (1 per week) to see how many fruits are produced by each tree as well
    as how many total fruits are produced.
    '''
    
    trees = []

    # create first tree
    tree_id = "Apple Tree"
    ft = FruitTree(tree_id) # using default values of 1 for max_fruits_per_day and watering_frequency
    ft.set_max_fruits_per_day(2) # set max fruits produced to 2 per day
    ft.set_watering_frequency(3) # set tree's suggested watering frequency to 3 times per week
    print(f"Tree '{tree_id}' can produce {ft.get_max_fruits_per_day()} fruits per day if watered {ft.get_watering_frequency()} times per week.")
    trees.append(ft) # add the tree to the list of trees.

    # create second tree
    tree_id = "Orange Tree"
    ft = FruitTree(tree_id) # using default values of 1 for max_fruits_per_day and watering_frequency
    ft.set_max_fruits_per_day(3) # set max fruits produced to 3 per day
    ft.set_watering_frequency(2) # set tree's suggested watering frequency to 2 times per week
    print(f"Tree '{tree_id}' can produce {ft.get_max_fruits_per_day()} fruits per day if watered {ft.get_watering_frequency()} times per week.")
    trees.append(ft) # add the tree to the list of trees.

    # Watering based on sugggested watering frequency
    print("\nWEEK 1: WATERING ACCORDING TO SUGGESTED FREQUENCY")
    for tree in trees:
        tree.reset() # reset the to starting condition. 
    FruitTree.total_fruits = 0 # reset the total combined fruits produced by all trees to 0

    # Watering a tree is distributed in a way to follow the suggested frequency.
    # Trees with a suggested watering frequency of 7 are watered every day;
    # those with suggested watering frequency of 6 are watered on days [0,1,2,3,4,5];
    # and so on...
    for day in range(7): # seven days of a week. day = 0 represents sunday
        print(f"DAY {day}:")
        for tree in trees:
            tree.begin_day() # start the day
            if tree.get_watering_frequency() == 7: 
                tree.water() # water the tree
            elif tree.get_watering_frequency() == 6 and day in [0,1,2,3,4,5]:
                tree.water()
            elif tree.get_watering_frequency() == 5 and day in [0,1,2,4,5]:
                tree.water()
            elif tree.get_watering_frequency() == 4 and day in [0,2,4,6]:
                tree.water()
            elif tree.get_watering_frequency() == 3 and day in [0,2,4]:
                tree.water()
            elif tree.get_watering_frequency() == 2 and day in [0,3]:
                tree.water()
            elif tree.get_watering_frequency() == 1 and day in [0]:
                tree.water()           
            
        for tree in trees:
            tree.end_day()
            print(tree)
    print(f"TOTAL FRUITS = {FruitTree.total_fruits}") # print total fruits produced by all the trees

    # Watering 1 time less per week
    print("\nWEEK 1: WATERING 1 TIME LESS THAN SUGGESTED FREQUENCY")
    for tree in trees:
        tree.reset() # reset tree to starting condition
    FruitTree.total_fruits = 0

    # Watering a tree is distributed in a way that the tree is watered one day less than suggested frequency
    for day in range(7):
        print(f"DAY {day}:")
        for tree in trees:
            tree.begin_day()
            if tree.get_watering_frequency() == 7 and day in [0,1,2,3,4,5]:
                tree.water()
            elif tree.get_watering_frequency() == 6 and day in [0,1,2,4,5]:
                tree.water()
            elif tree.get_watering_frequency() == 5 and day in [0,2,4,6]:
                tree.water()
            elif tree.get_watering_frequency() == 4 and day in [0,2,4]:
                tree.water()
            elif tree.get_watering_frequency() == 3 and day in [0,3]:
                tree.water()
            elif tree.get_watering_frequency() == 2 and day in [0]:
                tree.water()                
            
        for tree in trees:
            tree.end_day()
            print(tree)
    print(f"TOTAL FRUITS = {FruitTree.total_fruits}") # print total fruits produced by all the trees

    # Watering 1 time more per week
    print("\nWEEK 1: WATERING 1 TIME MORE THAN SUGGESTED FREQUENCY")
    for tree in trees:
        tree.reset() # reset tree to starting condition
    FruitTree.total_fruits = 0

    # Watering a tree is distributed in a way that the tree is watered one day more than suggested.
    for day in range(7): 
        print(f"DAY {day}:")
        for tree in trees:
            tree.begin_day()
            if tree.get_watering_frequency() == 7 or  tree.get_watering_frequency() == 6: 
                tree.water() # water the tree
            elif tree.get_watering_frequency() == 5 and day in [0,1,2,3,4,5]:
                tree.water()
            elif tree.get_watering_frequency() == 4 and day in [0,1,2,4,5]:
                tree.water()
            elif tree.get_watering_frequency() == 3 and day in [0,2,4,6]:
                tree.water()
            elif tree.get_watering_frequency() == 2 and day in [0,2,4]:
                tree.water()
            elif tree.get_watering_frequency() == 1 and day in [0,3]:
                tree.water()      
            
        for tree in trees:
            tree.end_day()
            print(tree)
    print(f"TOTAL FRUITS = {FruitTree.total_fruits}") # print total fruits prodcued by all the trees

if __name__ == "__main__":
    main()
