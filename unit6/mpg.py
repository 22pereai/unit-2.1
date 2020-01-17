#!/usr/bin/env python3

import csv

FILENAME = "trips.csv"

def write_trips(mpglist):
    with open(FILENAME, "a", newline="") as file: # write to CSV file
        writer = csv.writer(file)
        writer.writerows(mpglist)

def read_trips(mpglist):
    with open(FILENAME, newline="") as file: # read from CSV file
        reader = csv.reader(file)
        for row in reader:
            mpglist.append(row)
    return mpglist

def list_trips(mpglist):
    for i in range(len(mpglist)):
        if i == 0:
            print()
        else:
            mpg = mpglist[i]
            print(str(i) + ". " + str(mpg[0]), str(mpg[1]), str(mpg[2]))
    print()

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def main():
    mpglist = []
    read_trips(mpglist)
    list_trips(mpglist)
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        mpglist = [[miles_driven, gallons_used, mpg]]
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        write_trips(mpglist)
        read_trips(mpglist)
        print()
        list_trips(mpglist)
        
        more = input("More entries? (y or n): ")
    
    print("Bye")

if __name__ == "__main__":
    main()
