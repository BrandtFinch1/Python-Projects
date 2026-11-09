flight_price = 0.0
hotel_booking = 0.0
car_rental = 0.0
destination = "None"
has_flight = False
has_hotel = False
has_rental = False



while True:
    print("Welcome to the Travel Booking System")
    print("1. Book a flight")
    print("2. Book a hotel")
    print("3. Book a car rental")
    print("4. View booking details")
    print("5. Exit")
    print("Please select an option 1-5: ")

    try:
        num_input= int(input())


        if num_input==1:
            destination = input("Where are you heading? ")
            flight_price = float(input("Enter the price of your flight: "))
            has_flight = True
        
            print(f"Flight to {destination} booked for ${flight_price}")

        elif num_input==2:
            hotel_booking = float(input("Enter the price of the hotel: "))
            print(f"Hotel booked for ${hotel_booking}")
            has_hotel = True
    
        elif num_input==3:
            car_rental = float(input("Enter the price of the car rental: "))
            print(f"Car Rental booked for ${car_rental}")
            has_rental = True

        elif num_input==4:
            print("Booking Summary: ")
            print(f"Flight: ${flight_price}")
            print(f"Hotel: ${hotel_booking}")
            print(f"Car Rental: ${car_rental}")
            total_price= flight_price + hotel_booking + car_rental
            print(f"Total price before discount: ${total_price}")

            if has_flight == True and has_hotel == True and has_rental== True:
                first_operation_2 = total_price * 0.20
                print("Applied discount 20%")
                discount_20 = total_price - first_operation_2
                print(f"Total price after discount: ${discount_20}")

            elif has_flight == True and has_hotel == True:
            
                first_operation = total_price * 0.10
                print("Applied discount 10.0%")
                discount_10 = total_price - first_operation
                print(f"Total price after discount: ${discount_10}")

            

    
        elif num_input == 5:
        
            print("Thank you for using the Travel Booking System! Goodbye.")
            break
        


    except ValueError:
        print("Invalid Input")


