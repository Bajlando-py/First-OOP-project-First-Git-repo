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
    def rent_bike_on_hourly_bases(self, num_bikes):
        """Rents a bike on hourly bases."""
        if 0 >= num_bikes or num_bikes > self.__stock:
            print(f"There are not enough bikes available. We currently have {self.__stock} available.")
            return None
        else:
            rent_start = dt.datetime.now()
            print(
                f"You have rented {num_bikes} bike(s) on {rent_start.year}-{rent_start.month}-{rent_start.day} at {rent_start.hour}:{rent_start.minute} {rent_start.second}.")
            print("The charge is $5 per bike for 1 hour.\nEnjoy your ride.")
            self.__stock -= num_bikes
            return rent_start

    # TODO 4 - Create a method to rent bike on daily bases
    def rent_bike_on_daily_bases(self, num_bikes):
        """Rents a bike on daily bases."""
        if 0 >= num_bikes or num_bikes > self.__stock:
            print(f"There are not enough bikes available. We currently have {self.__stock} available.")
            return None
        else:
            rent_start = dt.date.today()
            print(f"You have rented {num_bikes} bike(s) on {rent_start}")
            print("The charge is $20 per bike for 1 day.\nEnjoy your ride.")
            self.__stock -= num_bikes
            return rent_start

    # TODO 5 - Create a method to rent bike on weekly bases
    def rent_bike_on_weekly_bases(self, num_bikes):
        """Rents a bike on weekly bases."""
        if 0 >= num_bikes or num_bikes > self.__stock:
            print(f"There are not enough bikes available. We currently have {self.__stock} available.")
            return None
        else:
            rent_start = dt.date.today()
            print(f"You have rented {num_bikes} bike(s) on {rent_start}")
            print("The charge is $60 per bike for 1 week.\nEnjoy your ride.")
            self.__stock -= num_bikes
            return rent_start

    # TODO 6 - Create a method to return bike from the system
    def return_bike(self, returns):
        """Adds bikes returned from customer, returns bill."""
        rent_start, rent_period, num_bikes = returns
        bill = 0
        if rent_start and rent_period and num_bikes:
            self.__stock += num_bikes
            rent_end = dt.datetime.now()
            rent_duration = rent_end - rent_start
            # Hourly bill calculation
            if rent_period == 1:
                bill = round(rent_duration.seconds / 3600) * 5 * num_bikes
            # Daily bill calculation
            elif rent_period == 2:
                bill = round(rent_duration.days) * 20 * num_bikes
            # Weekly bill calculation
            elif rent_period == 3:
                bill = round(rent_duration.days / 7) * 60 * num_bikes
            # 30% family discount 3-6 bikes rented
            if 2 < num_bikes < 7:
                print("You are eligible for family discount of 30%.")
                bill = bill * 0.7
            print("Thank you for returning the bikes. We hope you had a great time.")
            print(f"Your bill is: ${bill}.")
            return bill
        else:
            print("Please enter valid information.")
            return None


# TODO 7 - Create Customer Class and initialize attributes
class Customer:
    def __init__(self):
        """Intializer for customer class"""
        self.bikes = 0
        self.rental_bases = 0
        self.rental_time = 0
        self.bill = 0

    # TODO 8 - Create a method to request bike from the system
    def request_bike(self):
        """Takes a request from the customer for the number of bikes"""
        bikes = input("Please enter how many bikes do you want to rent: ")
        try:
            bikes = int(bikes)
        except:
            print("You need to enter valid positive number.")
            return -1
        if bikes < 1:
            print("You need to enter valid positive number.")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    # TODO 9 - Create a method to return bike to the system
    def return_bikes(self):
        """Allows customers to return their bikes to the rental shop"""
        if self.bikes and self.rental_bases and self.rental_time:
            return self.rental_time, self.rental_bases, self.bikes
        else:
            return 0, 0, 0


# TODO 10 - Main program logic : print options to the console

# TODO 11 - Ask from user to get option (check if it is int)

# TODO 12 - Based on selected choice call methods from Bike

customer1 = Customer()
print(customer1.bikes)
customer1.request_bike()
print(customer1.bikes)