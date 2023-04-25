import datetime as dt


# TODO 1 - Create Bike Rental Class and initialize stock attribute
class BikeRental:
    def __init__(self, stock=100):
        """Initializer for Bike rental class"""
        self.__stock = stock

    # TODO 2 - Create a method to display stock
    def display_stock(self):
        """Displays available bikes"""
        print(f"We have {self.__stock} bikes available for rent")
        return self.__stock

    # TODO 3 - Create a method to rent bike on hourly bases
    def rent_bike_on_hourly_basis(self, num_bikes):
        """Rents a bike on hourly bases."""
        if 0 >= num_bikes > self.__stock:
            print(f"There are not enough bikes available. We currently have {self.__stock} available.")
            return None
        else:
            rent_start = dt.datetime.now()
            print(f"You have rented {num_bikes} bike(s) on {rent_start.day}.{rent_start.month}.{rent_start.year} at {rent_start.hour}:{rent_start.minute}.")
            print("The charge is $5 per bike for 1 hour.\nEnjoy the ride.")
            self.__stock -= num_bikes
            return rent_start


# TODO 4 - Create a method to rent bike on daily bases

# TODO 5 - Create a method to rent bike on weekly bases

# TODO 6 - Create a method to return bike from the system

# TODO 7 - Create Customer Class and initialize attributes

# TODO 8 - Create a method to request bike from the system

# TODO 9 - Create a method to return bike to the system

# TODO 10 - Main program logic : print options to the console

# TODO 11 - Ask from user to get option (check if it is int)

# TODO 12 - Based on selected choice call methods from Bike

rental = BikeRental()
rental.display_stock()
rental.rent_bike_on_hourly_basis(8)
rental.display_stock()