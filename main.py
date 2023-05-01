import BikeRental as bk

# TODO 10 - Main program logic : print options to the console
system = bk.BikeRental(100)
customer = bk.Customer()

while True:
    print("""
    ====== Bike Rental App ======
    1. Enter 0 for available bikes.
    2. Enter 1 to rent bike(s) on hourly bases - $5
    3. Enter 2 to rent bike(s) on daily bases - $20
    4. Enter 3 to rent bike(s) on weekly bases  -$60
    5. Enter 4 to return bike(s)
    6. Enter 5 to exit the system
    """)

    # TODO 11 - Ask from user to get option (check if it is int)
    selection = input("Please enter your choice: ")
    print()
    try:
        selection = int(selection)
    except:
        print("You need to enter valid option")
        continue
    # TODO 12 - Based on selected choice call methods from Bike
    if selection == 0:
        system.display_stock()
    elif selection == 1:
        # req_bikes = customer.request_bike()
        # rent_start = system.rent_bike_on_hourly_bases(req_bikes)
        # customer.rental_time = rent_start
        customer.rental_time = system.rent_bike_on_hourly_bases(customer.request_bike())
        customer.rental_bases = 1
    elif selection == 2:
        customer.rental_time = system.rent_bike_on_daily_bases(customer.request_bike())
        customer.rental_bases = 2
    elif selection == 3:
        customer.rental_time = system.rent_bike_on_weekly_bases(customer.request_bike())
        customer.rental_bases = 3
    elif selection == 4:
        customer.bill = system.return_bike(customer.return_bikes())
        customer.rental_time, customer.rental_bases, customer.bikes = 0, 0, 0
    elif selection == 5:
        break
    else:
        print("You need to enter valid option")

print("Thank you for your business.")


